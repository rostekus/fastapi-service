from typing import Protocol

from app.relevance.model import RelevanceModel


class ModelDataBase(Protocol):
    def load(model_id: str) -> RelevanceModel:
        pass

    def save(model: RelevanceModel, model_id: str) -> None:
        pass
