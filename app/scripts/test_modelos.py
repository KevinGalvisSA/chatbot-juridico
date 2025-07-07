import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("Modelos disponibles con esta API key:\n")

for model in genai.list_models():
    print(f"- {model.name} ({model.supported_generation_methods})")
