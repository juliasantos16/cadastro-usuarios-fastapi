from abc import ABC, abstractclassmethod

class UserFinderInterface(ABC):

    @abstractclassmethod
    async def find_user_by_name(self, user_name: str ) -> dict:
        pass