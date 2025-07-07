from fastapi import FastAPI
from app.adapters.http.routes import router

app = FastAPI(title="Chatbot Jurídico - Constitución de Colombia")
app.include_router(router)
