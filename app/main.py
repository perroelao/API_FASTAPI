from fastapi import FastAPI
from app.routers import usuarios
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API gestion de usuarios",
    version="1.0.0",
    description="API para gestionar usuarios usando FASTAPI y ORACLE"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuarios.router)