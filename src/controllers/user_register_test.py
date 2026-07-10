from .user_register import UserRegister
import pytest

class UserRepositoryMock:
    def __init__ (self):
        self.insert_users_att = {}


    async def insert_users(self, user_data: dict ):
        self.insert_users_att['user_data'] = user_data



@pytest.mark.asyncio
async def test_register_user():
    user_repository = UserRepositoryMock()
    user_register = UserRegister(user_repository)

    user_data = {
        'user_name': 'Maria Silva',
        'age': 32,
        'uf': 'MG'
    }

    response = await user_register.register_user(user_data)


    assert user_repository.insert_users_att['user_data'] == user_data


    assert response['type'] == 'USERS'
    assert response['count'] == 1
    assert response['attributes'] == user_data