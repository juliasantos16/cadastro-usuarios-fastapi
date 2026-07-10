from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface

class UserRegister:
    def __init__(self, users_repositor: UsersRepositoryInterface) -> None:
        self.users_repository = users_repository