from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import mapper, registry, relationship

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
accounts = Table(
    "accounts",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("account_data", ForeignKey("accounts_data.id"), nullable=False),
    Column("socie_type", String(20)),
    Column("fees", String),
    Column("invoices", String),
    Column("socie", Boolean, default=True),
    Column("provider", Boolean, default=False),
)
def start_mappers():
    mapper_registry.map_imperatively(socies.AccountData, accounts_data)
    mapper_registry.map_imperatively(socies.Account, accounts)