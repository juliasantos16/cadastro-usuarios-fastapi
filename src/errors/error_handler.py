from fastapi import HTTPException
from .types.http_error import HttpError

def error_handler (exception: Exception) -> HTTPException:
    if isinstance (exception, HttpError):
        raise HTTPException (
            status_code=exception.status_code,
            detail=exception.message
        )
    raise HTTPException(
        status_code=500,
        detail="erro inesperado ao processar!!"
    )
