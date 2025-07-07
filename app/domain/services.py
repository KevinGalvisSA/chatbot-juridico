from app.infrastructure.qdrant.qdrant_client import get_relevant_chunks
from app.infrastructure.llm.llm_tool import answer_with_context

def generate_answer(question: str) -> str:
    chunks = get_relevant_chunks(question)
    return answer_with_context(question, chunks)
