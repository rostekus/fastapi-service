from fastapi import status
from fastapi.testclient import TestClient

from app.const import (
    MODEL_URL,
)
from app.main import app

client = TestClient(app)


def test_login(config):
    data = {

    "data": [1.0, 2.0, 3.0, 4.0, 7.0],
    "k": "1",
    "l" : "1"

}

    response = client.post("/" + MODEL_URL, data=data)
    schema = response.json()

    assert response.status_code == status.HTTP_200_OK

