from __future__ import annotations

import threading
from typing import Optional

from app.app.relevance.api import RelevanceModel

lock = threading.Lock()


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(Singleton, cls).__call__(
                        *args, **kwargs
                    )
        return cls._instances[cls]


class InMemoryModelDatabase(metaclass=Singleton):
    def __init__(self):
        self.models: dict[str, RelevanceModel] = {}

    def load(self, model_id: str) -> Optional[RelevanceModel]:
        return self.models[model_id]

    def save(self, model: RelevanceModel, model_id: str) -> None:
        self.models[model_id] = model

    def get_all(self) -> list[str]:
        return list(self.models.keys())


def create_inmemory_db_session() -> InMemoryModelDatabase:
    return InMemoryModelDatabase()
