from abc import ABC, abstractclassmethod



class UsersRepositoryInterface:

    @abstractclassmethod
    async def insert_users(self, user_infos: dict) -> None: pass

    @abstractclassmethod
    async def get_users_by_name(self, user_name: str) ->list[dict]: pass