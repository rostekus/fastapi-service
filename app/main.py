from fastapi import FastAPI

from app.const import OPEN_API_DESCRIPTION, OPEN_API_TITLE
from app.version import __version__

app = FastAPI(
    title=OPEN_API_TITLE,
    description=OPEN_API_DESCRIPTION,
    version=__version__,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
