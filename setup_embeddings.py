import fitz # type: ignore
from sentence_transformers import SentenceTransformer # type: ignore
from qdrant_client import QdrantClient # type: ignore
from qdrant_client.models import VectorParams, Distance, PointStruct # type: ignore
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

PDF_PATH = "docs/constitucion_colombia.pdf"
COLLECTION_NAME = "constitucion_colombia"
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

def extract_text(path: str) -> str:
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def split_text(text: str, max_len: int = 500) -> list[str]:
    chunks = []
    current = ""
    for paragraph in text.split("\n"):
        if len(current) + len(paragraph) < max_len:
            current += paragraph + " "
        else:
            chunks.append(current.strip())
            current = paragraph + " "
    if current:
        chunks.append(current.strip())
    return chunks

def upload_chunks(chunks: list[str]):
    model = SentenceTransformer("all-MiniLM-L6-v2")

    qdrant = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY if QDRANT_API_KEY else None,
    )

    if COLLECTION_NAME not in [c.name for c in qdrant.get_collections().collections]:
        qdrant.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )

    vectors = model.encode(chunks).tolist()
    points = [
        PointStruct(
            id=str(uuid.uuid4()),
            vector=vec,
            payload={"text": chunk}
        )
        for vec, chunk in zip(vectors, chunks)
    ]

    qdrant.upload_points(
        collection_name=COLLECTION_NAME,
        points=points,
    )

    print(f"✅ Subidos {len(points)} fragmentos a Qdrant.")

if __name__ == "__main__":
    print("📥 Extrayendo texto del PDF...")
    raw_text = extract_text(PDF_PATH)

    print("✂️ Dividiendo texto...")
    chunks = split_text(raw_text)

    print(f"📡 Subiendo {len(chunks)} fragmentos a Qdrant...")
    upload_chunks(chunks)
