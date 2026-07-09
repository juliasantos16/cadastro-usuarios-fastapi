from fastapi import APIRouter
from fastapi.responses import JSONResponse

users_routes = APIRouter(tags=['Usuários'])

@users_routes.post('/users')
async def criar_usuario():

    return JSONResponse(
        content={'olá': 'mundo'},
        status_code=200
    )