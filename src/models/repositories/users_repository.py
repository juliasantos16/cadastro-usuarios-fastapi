from src.models.entities.users import users
from src.models.settings.database_connection_handler import DBConnectionHandler
from sqlalchemy import insert, select, delete

class UsersRepository:
    async def insert_users(self, user_infos: dict) -> None:
        async with DBConnectionHandler() as db:
            query = insert(users).values(**user_infos)
            await db.session.execute(query)
            await db.session.commit()

    async def get_users_by_name(self, user_name: str) ->list[dict]:
        async with DBConnectionHandler() as db:
            query = (
                select(users)
                .where(users.c.user_name == user_name)
            )
            result = await db.session.execute(query)
            rows = result.fetchall()

            users_list = [dict(row._mapping) for row in rows]
            return users_list