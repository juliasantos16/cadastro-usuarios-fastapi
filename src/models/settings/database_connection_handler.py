# string de conexão -> aonde está o banco e onde está as credenciais
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import Optional

CONNECTION_STRING = f'sqlite+aiosqlite:///schema.db'

engine = create_async_engine(
    CONNECTION_STRING,
    echo=False, # -> Controla se o SQLAlchemy vai mostrar no terminal os comandos SQL executados.
    pool_size=2, # -> quantas conexões permanentes o pool mantém abertas.
    max_overflow=0, # -> quantas conexões extras podem ser criadas além do pool_size.
    pool_timeout=30 # -> quanto tempo uma requisição espera por uma conexão disponível antes de dar erro.
)

async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class DBConnectionHandler:
    def __init__(self) -> None:
        self.session: Optional[AsyncSession] = None

    async def __aenter__(self):
        self.session = async_session()
        return self

    async def __aexit__ (self, exc_type, exc_val, exc_tb):
        await self.session.close()

async with DBConnectionHandler() as db:
    db.session.commit()
