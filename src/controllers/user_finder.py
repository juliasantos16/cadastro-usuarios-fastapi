from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface
from src.errors.types.http_not_found import HttpNotFoundError
from .interfaces.user_finder import UserFinderInterface

class UserFinder (UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    async def find_user_by_name(self, user_name: str ) -> dict:
        users = await self.__users_repository.get_users_by_name(user_name)
        if not users:
            raise HttpNotFoundError("Usuário não encontrado")

        return {
            'type': 'USERS',
            'count': len(users),
            'attributes': users
        }
