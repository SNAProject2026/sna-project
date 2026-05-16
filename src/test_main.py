from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert b"inno-sna-project" in response.content


def test_api_hello():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_debug_status_code():
    response = client.get("/debug/500")
    assert response.status_code == 500
    assert response.content == b""


def test_metrics_endpoint():
    client.get("/api")
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "text/plain" in response.headers["content-type"]
    assert b"python_info" in response.content
    assert b"http_requests_total" in response.content
