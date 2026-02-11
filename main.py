import os
from pathlib import Path

def hydrate_project():
    # Use current directory as the project root
    base_path = Path.cwd()
    
    print(f"🛠️  Hydrating project in: {base_path}")

    # Define the sub-structure
    structure = {
        "app": ["main.py", "config.py", "database.py"],
        "app/models": ["__init__.py", "user.py", "organization.py", "workspace.py", "file.py", "audit.py"],
        "app/schemas": ["__init__.py", "auth.py", "workspace.py", "file.py", "chat.py"],
        "app/routes": ["__init__.py", "auth.py", "workspace.py", "file.py", "search.py", "chat.py"],
        "app/services": ["__init__.py", "auth_service.py", "file_service.py", "embedding_service.py", "rag_service.py"],
        "app/ai": ["__init__.py", "chunker.py", "embedder.py", "retriever.py"],
        "app/utils": ["__init__.py", "jwt.py", "logger.py"],
        "alembic": [],
        "migrations": [],
        "uploads": [],
    }

    # Create directories and files
    for folder, files in structure.items():
        dir_path = base_path / folder
        dir_path.mkdir(parents=True, exist_ok=True)
        for file in files:
            file_path = dir_path / file
            if not file_path.exists():
                file_path.touch()
                print(f"  Created: {folder}/{file}")

    # Root level files
    root_files = ["requirements.txt", "Dockerfile", ".env", ".gitignore"]
    for file in root_files:
        file_path = base_path / file
        if not file_path.exists():
            file_path.touch()
            print(f"  Created root file: {file}")

    # Injecting the FastAPI starter code into app/main.py
    main_file = base_path / "app" / "main.py"
    if main_file.stat().st_size == 0:
        main_content = """from fastapi import FastAPI
from app.routes import auth, chat, workspace

app = FastAPI(title="Veritas Aether API", version="0.1.0")

@app.get("/")
async def root():
    return {"status": "active", "service": "Veritas-Aether"}

# app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
"""
        main_file.write_text(main_content)

    print("\n✅ Structure is set. Time to start coding!")

if __name__ == "__main__":
    hydrate_project()