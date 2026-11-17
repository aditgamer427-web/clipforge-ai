
from fastapi import FastAPI

app = FastAPI(title="ClipForge AI")

@app.get("/")
def home():
    return {
        "message": "ClipForge AI backend is running!",
        "status": "online"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
  
