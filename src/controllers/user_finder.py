from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface

class UserFinder:
    def __init__(self, users_repositor: UsersRepositoryInterface) -> None:
        self.users_repository = users_repository

    async def find_user_by_name(self, name: str ) -> dict:
        users = await self.__users_repository.get_users_by_name(user_name)
        return {
            'type': 'USERS',
            'count': len(users),
            'attributes': users
        }