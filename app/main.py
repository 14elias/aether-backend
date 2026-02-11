from fastapi import FastAPI
from app.routes import auth, chat, workspace

app = FastAPI(title="Veritas Aether API", version="0.1.0")

@app.get("/")
async def root():
    return {"status": "active", "service": "Veritas-Aether"}

# app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
