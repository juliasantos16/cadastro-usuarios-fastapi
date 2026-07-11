from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
from .interfaces.user_register import UserRegisterInterface

class UserRegister(UserRegisterInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    async def register_user(self, user_data: dict) -> dict:
        self.__validate_user_data(user_data)
        await self.__registry_user(user_data)
        return self.__format_response(user_data)

    def __validate_user_data(self, user_data: dict)-> None:
        age = user_data["age"]
        uf = user_data["uf"].upper()

        if uf not in ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", 
                    "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", 
                    "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]:

            raise HttpUnprocessableEntityError("Estado inválido para cadastro")

        if age > 120:
            raise HttpUnprocessableEntityError("Idade inválida para cadastro")

    async def __registry_user(self, user_data: dict) -> None:
        await self.__users_repository.insert_users(user_data)

    def __format_response(self, user_data: dict) -> dict:
        return {
            'type': 'USERS',
            'count': 1,
            'attributes': user_data
        }