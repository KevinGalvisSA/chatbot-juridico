from fastapi import APIRouter
from app.application.usecases import ask_question

router = APIRouter(prefix="/api")

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.post("/ask")
def ask(question: str):
    response = ask_question(question)
    return {"response": response}
