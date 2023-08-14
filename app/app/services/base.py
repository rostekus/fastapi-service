from app.app.repository.api import ModelDataBase


class DataBaseProvider:
    """Provides instance of database session."""

    def __init__(self, db: ModelDataBase) -> None:
        self.db = db


class BaseService(DataBaseProvider):
    """Base class for application services."""
