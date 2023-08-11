from __future__ import annotations

import logging
from concurrent.futures import ThreadPoolExecutor

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import NearestNeighbors

logging.basicConfig(level=logging.INFO)


class ImplementationRelevanceModel:
    def train(
        self, input_data: list[float()], l: int, k: int, num_threads: int = 4
    ) -> None:
        self.model = []
        divided_datasets = self._devide_data(input_data, l)
        argument_sets = [(subset, k) for subset in divided_datasets]
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [
                executor.submit(self._calculate_representativeness, *args)
                for args in argument_sets
            ]
        for f in futures:
            logging.info(f.result())

    def _devide_data(self, input_data: list[float], l: int) -> list[list[float]]:
        if l <= 0:
            raise ValueError("Number of parts must be greater than 0.")
        if not len(input_data):
            raise ValueError("Empty list")

        data_copy = input_data.copy()
        return np.array_split(data_copy, l)

    def create_submodel_model(self, X: list[float], y: float):
        logging.info(X, y)
        X = np.array(X).reshape(-1, 1)  # Reshape X into a 2D array
        model = LinearRegression()
        model.fit(X, y)
        return model

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
        representativeness_scores = [1 / (1 + avg_dist) for avg_dist in avg_distances]
        self.model.append(self.create_submodel_model(arr, representativeness_scores))


# for FastAPI Depends on func
def create_implementation_relevence_model():
    return ImplementationRelevanceModel()
