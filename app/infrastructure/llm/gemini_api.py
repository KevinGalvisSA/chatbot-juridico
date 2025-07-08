import os
from dotenv import load_dotenv
import google.generativeai as genai # type: ignore
from app.domain.models import ContextChunk

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def answer_with_gemini(question: str, chunks: list[ContextChunk]) -> str:
    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro")

        context = "\n".join([chunk.text for chunk in chunks])
        prompt = f"""
Eres LEX (del latin "Ley"), un asistente jurídico experto en la Constitución Política de Colombia.

Usa el siguiente contexto para responder la pregunta del usuario de forma clara, precisa y confiable.

En caso de que la pregunta no tenga ninguna relacion con el tema al que estas diseñado. Responde que no estas autorizado para responder preguntas de ese tema

y estas unicamente diseñado para responder sobre la Constitución Política de Colombia.

Si por alguna razon la pregunta que te hacen no tiene coherencia o sentido alguno, responde unicamente "Tu pregunta no tiene correlacion alguno a temas de la Constitución Política de Colombia.

Si no sabes como respondes entonces di "Disculpa. No se como responder a tu pregunta".

Al terminar de responder una pregunta del usuario, siempre propon un tema de conversacion respecto a la Constitución Política de Colombia.

En caso de que el usuario se despida, responde con una despedida formal y no sugieras mas temas.".

### CONTEXTO:
{context}

### PREGUNTA:
{question}
"""

        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error al usar Gemini: {str(e)}"
