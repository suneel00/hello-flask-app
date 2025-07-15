import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_hello(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World!"

def test_app_exists():
    assert app is not None
    assert app.name == "app"
