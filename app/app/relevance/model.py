from __future__ import annotations

import concurrent.futures
import logging

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import NearestNeighbors

logging.basicConfig(level=logging.INFO)


class ImplementationRelevanceModel:
    def __init__(self, num_threads: int = 4):
        self.model: list[LinearRegression] = []
        self.n_thread: int = num_threads

    def train(self, input_data: list[float()], li: int, k: int) -> None:
        logging.info("begin training")

        divided_datasets = self._devide_data(input_data, li)
        argument_sets = [(subset, k) for subset in divided_datasets]
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.n_thread
        ) as executor:
            futures = [
                executor.submit(self._calculate_representativeness, *args)
                for args in argument_sets
            ]
        for future in concurrent.futures.as_completed(futures):
            _ = future.result()
        logging.info("done training")
        return self.predict(input_data)

    def _devide_data(
        self, input_data: list[float], li: int
    ) -> list[list[float]]:
        if li <= 0:
            raise ValueError("Number of parts must be greater than 0.")
        if not len(input_data):
            raise ValueError("Empty list")

        data_copy = input_data.copy()
        return np.array_split(data_copy, li)

    def create_submodel_model(self, X: list[float], y: float):
        X = np.array(X).reshape(-1, 1)  # Reshape X into a 2D array
        model = LinearRegression()
        model.fit(X, y)
        return model

    def predict(self, X: list[float]) -> list[float]:
        if not len(self.model):
            raise ValueError("there is no model trained")
        X = np.array(X).reshape(-1, 1)  # Reshape X into a 2D array
        data = []
        for model in self.model:
            data.append(model.predict(X))

        y = np.mean(np.array(data), axis=0)
        return y

    def _calculate_representativeness(
        self, arr: list[float], k_neighbors: int
    ) -> list[float]:
        model = NearestNeighbors(n_neighbors=k_neighbors)
        model.fit(np.array(arr).reshape(-1, 1))
        avg_distances = []
        for point in arr:
            distances, _ = model.kneighbors([[point]])
            avg_distance = np.mean(distances)
            avg_distances.append(avg_distance)
        representativeness_scores = [
            1 / (1 + avg_dist) for avg_dist in avg_distances
        ]
        self.model.append(
            self.create_submodel_model(arr, representativeness_scores)
        )


# for FastAPI Depends on func
def create_implementation_relevence_model():
    return ImplementationRelevanceModel()
