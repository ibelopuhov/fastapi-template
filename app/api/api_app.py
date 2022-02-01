from pathlib import Path
import logging

import uvicorn

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.api.models import *
from app.api.settings import settings
from .custom_logging import CustomizeLogger

# TODO - make config pedantic friandly with ability to change log file path and log levels
# Init custom logger

logger = logging.getLogger(__name__)
config_path = Path(__file__).with_name("logging_config.json")

def create_fast_api_app() -> FastAPI:

    tags_metadata = [
        {
            "name":"settings",
            "description": "Выводит в JSON-формате текущие настройки API"
        },{
            "name":"post_ex",
            "description": "Пример запроса POST"
        }
    ]

    app = FastAPI(
        title = "API 🚀 шаблон.",
        version = "0.0.1",
        description = "API 🚀 позволяет делать...",
        openapi_tags=tags_metadata
    )

    logger = CustomizeLogger.make_logger(config_path=config_path)
    app.logger = logger

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


app = create_fast_api_app()

@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn.access")
    
    console_formatter = uvicorn.logging.ColourizedFormatter(
        "{levelprefix} {asctime}: {message}",
        style="{", use_colors=True)
    logger.handlers[0].setFormatter(console_formatter)
    logger.info("Startup event here...")

@app.get("/api/settings", tags=["settings"])
def get_current_config_settings(request: Request):
    """
    Возвращает текущие настройки сервиса
    """
    request.app.logger.info("Возвращает текущие настройки сервиса")

    return {
        "settings": settings
    }

@app.post("/post_example", tags=["post_ex"])
def post_example(payload: InData):
    """
    POST example
    """
    return {"resp": payload}

