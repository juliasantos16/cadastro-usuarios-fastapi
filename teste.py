from fastapi import HTTPException
from .types.http_bad_request import HttpBadRequestError

def error_handler (exception: Exception) -> HTTPException:
    if isinstance (exception, HttpBadRequestError):



        raise HTTPException (
            status_code=exception.status_code,
            detail=exception.message
        )
    raise HTTPException(
        status_code=500,
        detail="erro inesperado ao processar!!"
    )