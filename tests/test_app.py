import pytest
from app import app  # Update the import path based on your project structure

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Welcome to the Flask App!"}

def test_add(client):
    """Test the add route."""
    response = client.get('/add/3/4')
    assert response.status_code == 200
    assert response.get_json() == {"result": 7}
