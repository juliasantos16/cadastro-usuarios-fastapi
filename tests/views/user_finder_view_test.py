import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.user_finder_view import UserFinderView


class UserFinderControllerMock:
    def __init__(self) -> None:
        self.find_user_by_name_att = {}

    async def find_user_by_name(self, user_name: str) -> dict:
        self.find_user_by_name_att['user_name'] = user_name
        return {
            "type": "USERS",
            "count": 1,
            "attributes": [{"user_name": user_name}]
        }


@pytest.mark.asyncio
async def test_handle_find_user_by_name():
    # Arrange
    controller = UserFinderControllerMock()
    view = UserFinderView(controller)
    http_request = HttpRequest(path_params={"user_name": "John Doe"})

    # Act
    http_response = await view.handle_find_user_by_name(http_request)

    # Assert
    assert controller.find_user_by_name_att['user_name'] == "John Doe"
    assert http_response.status_code == 200
    assert http_response.body == {
        "type": "USERS",
        "count": 1,
        "attributes": [{"user_name": "John Doe"}]
    }


@pytest.mark.asyncio
async def test_handle_find_user_by_name_error():
    from fastapi import HTTPException
    from src.errors.types.http_not_found import HttpNotFoundError

    class UserFinderControllerErrorMock:
        async def find_user_by_name(self, user_name: str) -> dict:
            raise HttpNotFoundError("Usuário não encontrado")

    controller = UserFinderControllerErrorMock()
    view = UserFinderView(controller)
    http_request = HttpRequest(path_params={"user_name": "John Doe"})

    # Act & Assert
    with pytest.raises(HTTPException) as excinfo:
        await view.handle_find_user_by_name(http_request)

    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "Usuário não encontrado"
