from abc import ABC, abstractclassmethod

class UserRegisterInterface(ABC):
    @abstractclassmethod
    async def register_user(self, user_data: dict) -> dict:
        pass