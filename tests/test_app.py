# tests/test_app.py
from fastapi.testclient import TestClient
from src.app import create_app
def test_read_root():
    app = create_app()
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello, AtlasDoc Ops!'}