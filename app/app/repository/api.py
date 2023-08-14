from __future__ import annotations

from typing import Protocol

from app.app.relevance.api import RelevanceModel


class ModelDataBase(Protocol):
    def load(model_id: str) -> RelevanceModel:
        pass

    def save(model: RelevanceModel, model_id: str) -> None:
        pass

    def get_all() -> list[str]:
        pass
