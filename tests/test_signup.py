import requests


def test_signup():
    response = requests.post(
        "http://localhost:5000/api/v1/signup",
        json={
            "age": 21,
            "name": "Gandab",
            "surname": "Hasanova",
            "username": "Gandab123",
            "email": "gandab@gmail.com",
            "gender": "F",
            "password": "Gandab123"
        }
    )
    
    assert response.status_code == 200
