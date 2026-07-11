import pytest
from fastapi import HTTPException
from src.errors.error_handler import error_handler
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError

def test_error_handler_bad_request():
    error = HttpBadRequestError("Invalid query parameter")
    
    with pytest.raises(HTTPException) as excinfo:
        error_handler(error)
        
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "Invalid query parameter"

def test_error_handler_not_found():
    error = HttpNotFoundError("Resource not found")
    
    with pytest.raises(HTTPException) as excinfo:
        error_handler(error)
        
    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "Resource not found"

def test_error_handler_unprocessable_entity():
    error = HttpUnprocessableEntityError("Validation failed")
    
    with pytest.raises(HTTPException) as excinfo:
        error_handler(error)
        
    assert excinfo.value.status_code == 422
    assert excinfo.value.detail == "Validation failed"

def test_error_handler_generic_exception():
    error = Exception("Database connection failure")
    
    with pytest.raises(HTTPException) as excinfo:
        error_handler(error)
        
    assert excinfo.value.status_code == 500
    assert excinfo.value.detail == "erro inesperado ao processar!!"
