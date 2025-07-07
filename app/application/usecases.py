from app.domain.services import generate_answer

def ask_question(question: str) -> str:
    return generate_answer(question)
