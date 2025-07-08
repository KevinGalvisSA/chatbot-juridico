from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from app.adapters.http.routes import router

# Crear la aplicación FastAPI
app = FastAPI(title="Chatbot Jurídico - Constitución de Colombia")

# Configuración de CORS
origins = [
    "http://localhost:5173",  # Frontend
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Especifica los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)

# Incluir las rutas definidas en `routes.py`
app.include_router(router)
