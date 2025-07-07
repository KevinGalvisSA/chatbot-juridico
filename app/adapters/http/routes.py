from fastapi import APIRouter
from pydantic import BaseModel
from app.application.usecases import ask_question

router = APIRouter(prefix="/api")

class AskRequest(BaseModel):
    question: str

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.post("/ask")
def ask(payload: AskRequest):
    response = ask_question(payload.question)
    return {"response": response}
