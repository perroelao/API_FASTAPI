from fastapi import FastAPI
from app.routers import usuarios

app = FastAPI(
    title="API gestion de usuarios",
    version="1.0.0",
    description="API para gestionar usuarios usando FASTAPI y ORACLE"
)

app.include_router(usuarios.router)