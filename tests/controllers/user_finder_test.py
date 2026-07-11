import pytest
from src.controllers.user_finder import UserFinder


class UserRepositoryMock:
    def __init__ (self):
        self.get_users_by_name_att = {}

    async def get_users_by_name(self, user_name: str) -> list[dict]:
        self.get_users_by_name_att['user_name'] = user_name
        return [{'user_name': 'olá'}, {'user_name': 'mundo'}]

@pytest.mark.asyncio
async def test_find_user_by_name():
    user_repo = UserRepositoryMock()
    user_finder = UserFinder(user_repo)
    user_name = 'Beltrano'

    response = await user_finder.find_user_by_name(user_name)

    assert user_repo.get_users_by_name_att['user_name'] == user_name

    assert response ['type'] == 'USERS'
    assert response ['count'] == 2
    assert 'attributes' in response
    assert isinstance (response['attributes'], list)


@pytest.mark.asyncio
async def test_find_user_by_name_not_found():
    from src.errors.types.http_not_found import HttpNotFoundError

    class UserRepositoryEmptyMock:
        async def get_users_by_name(self, user_name: str) -> list[dict]:
            return []

    user_repo = UserRepositoryEmptyMock()
    user_finder = UserFinder(user_repo)
    user_name = 'Inexistente'

    with pytest.raises(HttpNotFoundError) as excinfo:
        await user_finder.find_user_by_name(user_name)

    assert str(excinfo.value) == "Usuário não encontrado"
    assert excinfo.value.status_code == 404
    assert excinfo.value.name == "NotFoundError"
