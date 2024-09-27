from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_predict_good():
    user_id = {
        "user_id": 1
    }

    response = client.post("/get_predict", json=user_id)
    assert list(response.json().keys()) == ["status", "data"]
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert type(response.json()["data"]) == list
    assert len(response.json()["data"]) == 7


def test_get_predict_bad():
    user_id = {
        "user_id": 42
    }

    response = client.post("/get_predict", json=user_id)
    assert list(response.json().keys()) == ["status", "message"]
    assert response.status_code == 200
    assert response.json()["status"] == "error"
    assert type(response.json()["message"]) == str
    assert response.json()["message"] == "ID not in table"