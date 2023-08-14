import pytest
from fastapi import status
from fastapi.testclient import TestClient

from app.app.schemas.model import TrainingDataRequestSchema
from app.const import MODEL_URL
from app.main import app

#
client = TestClient(app)


def test_model_predict_and_saved():
    """Story:
    [Who]   As a API user
    [What] I want to train model and check if it was saved
    [Value] So I can later use it for calculating
    """
    data = {"data": [1.0, 2.0, 3.0, 4.0, 7.0], "k": 1, "l": 1}
    response = client.post("model/train", json=data)
    body = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert body["data"] == [1.0, 1.0, 1.0, 1.0, 1.0]

    model_id = body["message"]["id"]

    assert model_id != ""

    response = client.get("model")

    body = response.json()

    assert model_id in body["data"]


def test_number_of_saved_model():
    response = client.get("model")
    body = response.json()
    assert len(body["data"]) == 1


def test_use_saved_model_to_calculate():
    """Story:
    [Who]   As a API user
    [What] I want to retrive models id and use it for calculating relevance
    [Value]  I can use saved model
    """
    response = client.get("model")
    body = response.json()
    model_id = body["data"][0]
    data = {
        "id": model_id,
        "data": [1.0, 2.0, 3.0, 4.0, 7.0],
    }
    response = client.post("model/predict", json=data)
    body = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert body["data"] == [1.0, 1.0, 1.0, 1.0, 1.0]
