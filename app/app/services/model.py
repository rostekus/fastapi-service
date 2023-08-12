from __future__ import annotations

import logging
import uuid

from app.relevance.model import create_implementation_relevence_model
from app.services.base import BaseService

logging.basicConfig(level=logging.INFO)


class ModelService(BaseService):
    def train(
        self, training_data: list[float], li: int, k: int
    ) -> tuple[list[float], str]:
        """Train model and save to db"""
        if li <= 0 or  k <= 0 or  k > li:
            raise ValueError("incorrect k l num")
        model = create_implementation_relevence_model()
        model_id = str(uuid.uuid4())
        self.db.save(model, model_id)
        return model.train(training_data, li, k), model_id

    def predict(self, predict_data: list[float], model_id: str) -> list[float]:
        """Predict relevence using saved model"""
        model = self.db.load(model_id)
        predicted = model.predict(predict_data)
        return predicted
