from src.models.settings.metadata import metadata
from sqlalchemy import Table, Column

users = Table (
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_name", String, nullable=True),
    Column("age", Integer),
    Column("uf", String)
)
