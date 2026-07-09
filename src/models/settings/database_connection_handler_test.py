import pytest
from .database_connection_handler import DBConnectionHandler

@pytest.mark.asyncio
async def test_connection():
    async with DBConnectionHandler() as db_handler:
        print()
        assert db_handler.session is not None