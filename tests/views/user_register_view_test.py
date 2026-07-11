import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.user_register_view import UserRegisterView


class UserRegisterControllerMock:
    def __init__(self):
        self.register_user_att = {}

    async def register_user(self, user_data: dict) -> dict:
        self.register_user_att['user_data'] = user_data
        return {
            "type": "USERS",
            "count": 1,
            "attributes": user_data
        }


@pytest.mark.asyncio
async def test_handle_register_user():

    controller = UserRegisterControllerMock()
    view = UserRegisterView(controller)
    
    user_data = {
        "user_name": "Jane Doe",
        "age": 25,
        "uf": "SP"
    }
    http_request = HttpRequest(body=user_data)

    # Act
    http_response = await view.handle_register_user(http_request)

    # Assert
    assert controller.register_user_att['user_data'] == user_data
    assert http_response.status_code == 201
    assert http_response.body == {
        "type": "USERS",
        "count": 1,
        "attributes": user_data
    }


@pytest.mark.asyncio
async def test_handle_register_user_error():
    from fastapi import HTTPException

    class UserRegisterControllerErrorMock:
        async def register_user(self, user_data: dict) -> dict:
            raise Exception("Erro banco de dados ou validação")

    controller = UserRegisterControllerErrorMock()
    view = UserRegisterView(controller)
    
    user_data = {
        "user_name": "Jane Doe",
        "age": 25,
        "uf": "SP"
    }
    http_request = HttpRequest(body=user_data)

    # Act & Assert
    with pytest.raises(HTTPException) as excinfo:
        await view.handle_register_user(http_request)

    assert excinfo.value.status_code == 500
    assert excinfo.value.detail == "erro inesperado ao processar!!"
