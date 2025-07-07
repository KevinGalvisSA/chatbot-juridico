import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from app.domain.models import ContextChunk

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

qdrant = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
model = SentenceTransformer("all-MiniLM-L6-v2")
COLLECTION_NAME = "constitucion_colombia"

def get_relevant_chunks(query: str, top_k: int = 5):
    query_vector = model.encode(query).tolist()
    hits = qdrant.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=top_k
    )
    return [ContextChunk(hit.payload['text'], hit.score) for hit in hits]
