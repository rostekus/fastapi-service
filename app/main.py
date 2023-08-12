from __future__ import annotations

from const import OPEN_API_DESCRIPTION, OPEN_API_TITLE
from fastapi import FastAPI
from version import __version__

from app.routers.model import router as model_router

app = FastAPI(
    title=OPEN_API_TITLE,
    description=OPEN_API_DESCRIPTION,
    version=__version__,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.include_router(model_router)

traing = ""


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
