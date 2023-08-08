from typing import Protocol


class RelevanceModel(Protocol):
    def predict(input_data: list[float]) -> list[float]:
        pass
