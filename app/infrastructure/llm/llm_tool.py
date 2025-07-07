from app.domain.models import ContextChunk

def answer_with_context(question: str, chunks: list[ContextChunk]) -> str:
    context = "\n".join([chunk.text for chunk in chunks])
    return f"Respuesta simulada usando contexto:\n\n{context}\n\nPregunta: {question}"
