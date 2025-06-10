import os

from fastapi import FastAPI
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from app.api.v1 import routes
from app.core.config import settings

app = FastAPI(
    title=settings.api_title,
    description=settings.api_description,
    version=settings.api_version,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
static_path = os.path.join(BASE_DIR, "static")

app.mount("/static", StaticFiles(directory=static_path), name="static")
app.include_router(routes.router, prefix="/api/v1")


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(static_path + "/favicon.ico")
