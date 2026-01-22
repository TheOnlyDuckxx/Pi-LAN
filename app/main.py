"""Utilite: point d'entree FastAPI; fonctionnement: cree l'app, monte routes API/web et static."""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.router import api_router
from app.config import get_settings
from app.store.db import init_db
from app.web.pages import web_router


templates = Jinja2Templates(directory="app/web/templates")


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title="LANHub")

    app.include_router(api_router, prefix="/api")
    app.include_router(web_router)

    app.mount("/static", StaticFiles(directory="app/web/static"), name="static")

    @app.on_event("startup")
    async def _startup() -> None:
        await init_db(settings.db_path)

    return app


app = create_app()
