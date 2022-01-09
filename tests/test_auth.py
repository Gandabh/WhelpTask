import requests

def test_auth():
    response = requests.post(
        "http://localhost:5000/api/v1/auth",
        json={
            "username": "Gandab",
            "password": "Gandab123"
        }
    )

    assert response.status_code == 200
