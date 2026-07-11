from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from src.main.routes.users_routes import users_routes

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    formatted_errors = []
    for error in exc.errors():
        loc = error.get("loc", [])
        field = loc[-1] if loc else "field"
        msg = error.get("msg", "valor inválido")
        formatted_errors.append(f"'{field}': {msg}")
    
    detail = ", ".join(formatted_errors)
    return JSONResponse(
        status_code=422,
        content={
            "errors": [
                {
                    "title": "UnprocessableEntity",
                    "detail": detail
                }
            ]
        }
    )

app.include_router(users_routes)
