from typing import Protocol


class RelevanceModel(Protocol):
    def predict(self, input_data: list[float]) -> list[float]:
        pass

    def train(self, input_data: list[float()], li: int, k: int) -> None:
        pass
