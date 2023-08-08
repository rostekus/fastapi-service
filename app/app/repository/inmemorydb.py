from typing import Optional

from app.relevance.api import RelevanceModel


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class InMemoryModelDatabase(Singleton):
    def __init__(self):
        self.models: dict[str, RelevanceModel] = {}

    def load(self, model_id: str) -> Optional[RelevanceModel]:
        return self.model.get(model_id)

    def save(self, model: RelevanceModel, model_id: str) -> None:
        self.model[model_id] = model


def create_inmemory_db_session() -> InMemoryModelDatabase:
    return InMemoryModelDatabase()
