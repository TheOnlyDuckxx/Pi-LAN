"""Utilite: routes HTML; fonctionnement: rend les templates Jinja2 pour les pages."""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.store.repo import list_clients

router = APIRouter()
web_router = router

templates = Jinja2Templates(directory="app/web/templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/clients", response_class=HTMLResponse)
async def clients(request: Request):
    data = await list_clients()
    return templates.TemplateResponse("clients.html", {"request": request, "clients": data})


@router.get("/diagnostics", response_class=HTMLResponse)
async def diagnostics(request: Request):
    return templates.TemplateResponse("diagnostics.html", {"request": request})


@router.get("/games", response_class=HTMLResponse)
async def games(request: Request):
    return templates.TemplateResponse("games.html", {"request": request})
