from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import registry, mapper, relationship
from humanes_api.humanes.domain import socies

mapper_registry = registry()


accounts_data = Table(
    "accounts_data",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(50)),
    Column("last_name", String(50)),
    Column("venture", String(50)),
    Column("dni", String(50)),
    Column("zip_code", String(50)),
    Column("address", String(50)),
    Column("phone", String(50)),
    Column("email", String(50)),
)

def start_mappers():
    mapper_registry.map_imperatively(socies.AccountData, accounts_data)
