from fastapi import APIRouter, Depends

from app.repository.inmemorydb import (InMemoryModelDatabase,
                                       create_inmemory_db_session)
from app.schemas.model import (RelevanceResponseSchema,
                               TrainingDataRequestSchema)
from app.services.model import ModelService
from const import MODEL_URL

router = APIRouter(prefix="/" + MODEL_URL)


def get_database(db: InMemoryModelDatabase =
                 Depends(create_inmemory_db_session)):
    return db


@router.post("")
async def calculate_relevance(
    training_data: TrainingDataRequestSchema,
    db: InMemoryModelDatabase = Depends(get_database),
):
    data = ModelService(db).calculate_relevance([])
    return RelevanceResponseSchema(data=data)
