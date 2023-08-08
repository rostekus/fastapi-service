from typing import Protocol

from app.relevance.api import RelevanceModel


class ModelDataBase(Protocol):
    def load(model_id: str) -> RelevanceModel:
        pass

    def save(model: RelevanceModel, model_id: str) -> None:
        pass
