from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse, Response
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Python Web Server")
Instrumentator(excluded_handlers=["/metrics"]).instrument(app)

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


@app.get("/debug/{return_code}")
def debug_status(return_code: int):
    return Response(status_code=return_code)


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
