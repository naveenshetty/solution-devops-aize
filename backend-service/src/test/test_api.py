import pytest
from api import create_app

app = create_app()

@pytest.fixture
def client():
    with app.test_client() as client:
        app.testing = True
        yield client

# def test_home(client):
#     response = client.get('/')
#     assert response.status_code == 200
#     assert response.data.decode() == "Simple API Service"

def test_print(client):
    response = client.post('/print', json={'message': 'Hello, World!'})
    assert response.status_code == 200
    assert response.json == {"print": "Hello, World!"}

def test_print_no_message(client):
    response = client.post('/print', json={})
    assert response.status_code == 400
    assert response.json == {"error": "No message provided"}

def test_add_numbers(client):
    response = client.get('/add?num1=5&num2=10')
    assert response.status_code == 200
    assert response.json == {"result": 15.0}

def test_add_numbers_invalid_input(client):
    response = client.get('/add?num1=&num2=')
    assert response.status_code == 400
    assert response.json == {"error": "Both numbers are required"}

def test_get_user(client):
    response = client.get('/user/1')
    assert response.status_code == 200
    assert response.json == {"name": "Yoru", "email": "yoru@example.com"}

def test_get_user_not_found(client):
    response = client.get('/user/999')
    assert response.status_code == 404
    assert response.json == {"error": "User not found"}

def test_status(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.data.decode() == 'OK'

def test_get_config(client):
    response = client.get('/config')
    assert response.status_code == 200
    assert response.json == {
        "LOGGING_LEVEL": "INFO",
        "COUNT_VALUE": 0,
        "USER_NAME": "default"
    }
