import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_hello(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_app_exists():
    assert app is not None
    assert app.name == "app.app"
