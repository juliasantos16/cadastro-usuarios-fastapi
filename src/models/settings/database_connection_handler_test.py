import pytest
from .database_connection_handler import DBConnectionHandler

@pytest.mark.asyncio # Teste de integração
@pytest.mark.skip(reason="connecting with db")
async def test_connection():
    async with DBConnectionHandler() as db_handler:
        print()
        assert db_handler.session is not None