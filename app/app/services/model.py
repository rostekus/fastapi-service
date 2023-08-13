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
        """
        Train the relevance model and save it to the database.

        Args:
            training_data (list[float]): List of training data points.
            li (int): The number of subsets to divide the training data into.
            k (int): The number of nearest neighbors
            to consider when calculating distance.

        Returns:
            tuple[list[float], str]: A tuple containing
            a list of trained model results and the generated model ID.

        Raises:
            ValueError: If `li` or `k` are not within the valid range.
        """
        if li <= 0 or k <= 0 or k > li:
            raise ValueError("incorrect k l num")
        model = create_implementation_relevence_model()
        model_id = str(uuid.uuid4())
        self.db.save(model, model_id)
        return model.train(training_data, li, k), model_id

    def predict(self, predict_data: list[float], model_id: str) -> list[float]:
        """
        Predict relevance using a saved model.

        Args:
            predict_data (list[float]): List of data points
            to predict relevance for.
            model_id (str): The ID of the saved model to use for prediction.

        Returns:
            list[float]: List of predicted relevance
            scores for the input data points.
        """
        model = self.db.load(model_id)
        predicted = model.predict(predict_data)
        return predicted
