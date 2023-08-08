from pydantic import BaseModel


class TrainingDataRequestSchema(BaseModel):
    data: list[float]


class RelevanceResponseSchema(BaseModel):
    data: list[float]
