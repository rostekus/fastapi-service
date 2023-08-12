from __future__ import annotations

from pydantic import BaseModel


class TrainingDataRequestSchema(BaseModel):
    data: list[float]
    k: int
    l: int


class RelevanceResponseSchema(BaseModel):
    data: list[float] = []
    message: dict[str, str] = {}


class PredictDataRequestSchema(BaseModel):
    data: list[float]
    id: str


class PredictDataResponseSchema(BaseModel):
    data: list[float]


class GetAllModelsResponseSchema(BaseModel):
    data: list[str]
