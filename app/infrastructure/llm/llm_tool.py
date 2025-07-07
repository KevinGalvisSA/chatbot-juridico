from app.domain.models import ContextChunk
from app.infrastructure.llm.gemini_api import answer_with_gemini

def answer_with_context(question: str, chunks: list[ContextChunk]) -> str:
    return answer_with_gemini(question, chunks)
