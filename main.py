
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from urllib.parse import urlparse

app = FastAPI(title="ClipForge AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://aditgamer427-web.github.io"
    ],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class ClipRequest(BaseModel):
    video_url: str
    language: str
    count: int = 10

@app.get("/")
def home():
    return {
        "message": "ClipForge AI backend is running!",
        "status": "online"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/api/clip")
def create_clip(request: ClipRequest):
    parsed = urlparse(request.video_url)

    if parsed.hostname not in [
        "youtube.com",
        "www.youtube.com",
        "m.youtube.com",
        "youtu.be",
        "www.youtu.be"
    ]:
        return {
            "status": "error",
            "message": "Invalid YouTube URL."
        }

    return {
        "status": "not_ready",
        "message": "Backend received your request successfully, but video processing is not implemented yet.",
        "video_url": request.video_url,
        "language": request.language,
        "count": request.count
    }

  
