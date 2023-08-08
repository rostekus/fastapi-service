from fastapi import FastAPI

from app.routers.model import router as model_router
from const import OPEN_API_DESCRIPTION, OPEN_API_TITLE
from version import __version__

app = FastAPI(
    title=OPEN_API_TITLE,
    description=OPEN_API_DESCRIPTION,
    version=__version__,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.include_router(model_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
