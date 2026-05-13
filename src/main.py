from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(title="Python Web Server")

_STATIC_DIR = Path(__file__).resolve().parent.parent / "static"
_INDEX_HTML = _STATIC_DIR / "index.html"


@app.get("/")
def read_root():
    return FileResponse(_INDEX_HTML, media_type="text/html")


@app.get("/api")
def api_hello():
    return {"message": "Hello World"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
