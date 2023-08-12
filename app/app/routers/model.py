from __future__ import annotations

import asyncio
import logging
import traceback
from datetime import datetime
from http import HTTPStatus

from const import MODEL_URL
from fastapi import APIRouter, Depends, HTTPException

from app.repository.api import ModelDataBase
from app.repository.inmemorydb import (InMemoryModelDatabase,
                                       create_inmemory_db_session)
from app.schemas.model import (GetAllModelsResponseSchema,
                               PredictDataRequestSchema,
                               PredictDataResponseSchema,
                               RelevanceResponseSchema,
                               TrainingDataRequestSchema)
from app.services.model import ModelService

logging.basicConfig(level=logging.INFO)
router = APIRouter(prefix="/" + MODEL_URL)

# global state of training process
training_status = {
    "status": "none",
    "start_time": None,
}

training_status_lock = asyncio.Lock()


def get_database(
    db: InMemoryModelDatabase = Depends(create_inmemory_db_session),
):
    return db


@router.get("", response_model=GetAllModelsResponseSchema)
async def get_models(db: ModelDataBase = Depends(get_database)):
    return GetAllModelsResponseSchema(data=db.get_all())


@router.post("/predict")
async def predict(
    predict_data: PredictDataRequestSchema,
    db: ModelDataBase = Depends(get_database),
):
    try:
        data = ModelService(db).predict(predict_data.data, predict_data.id)

    except Exception as e:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"{timestamp} - {e}"
        logging.error(traceback.print_exc())
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=error_message
        )
    return PredictDataResponseSchema(data=data)


@router.post("/train", response_model=RelevanceResponseSchema)
async def train(
    training_data: TrainingDataRequestSchema,
    db: ModelDataBase = Depends(get_database),
):
    global training_status

    if training_status["status"] == "in_progress":
        return RelevanceResponseSchema(message=training_status.copy())

    async with training_status_lock:
        if training_status["status"] == "none":
            training_status["status"] = "in_progress"
            training_status["start_time"] = str(
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
    try:
        data, model_id = ModelService(db).train(training_data.data, 1, 1)
        # simulate long time processing
        await asyncio.sleep(10)
    except Exception as e:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"{timestamp} - {str(e)}"
        logging.error(traceback.print_exc())
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=error_message
        )
    training_status["status"] = "done"
    msg = {"id": model_id, **training_status.copy()}
    response = RelevanceResponseSchema(data=data, message=msg)
    training_status["status"] = "none"

    return response
