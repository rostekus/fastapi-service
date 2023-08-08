from typing import Optional

from app.relevance.model import RelevanceModel


class InMemeryModelDatabase:
    def __init__(self):
        self.models: dict[str, RelevanceModel] = {}

    def load(self, model_id: str) -> Optional[RelevanceModel]:
        return self.model.get(model_id)

    def save(self, model: RelevanceModel, model_id: str) -> None:
        self.model[model_id] = model
