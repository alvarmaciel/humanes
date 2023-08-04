from sqlalchemy import JSON, Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import mapper, registry, relationship

from humanes_api.humanes.domain.socies import Account, AccountData

mapper_registry = registry()


accounts_data_tbl = Table(
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
accounts_tbl = Table(
    "accounts",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("account_data_id", Integer, ForeignKey("accounts_data.id"), nullable=False),
    Column("socie_type", String(20)),
    Column("fees", JSON),
    Column("invoices", JSON),
    Column("activated", Boolean, default=True),
    Column("socie", Boolean, default=True),
    Column("provider", Boolean, default=False),
)

mapper_registry.map_imperatively(
    AccountData,
    accounts_data_tbl,
    properties={"accounts": relationship(Account, backref="account_data", order_by=accounts_tbl.c.id)},
)
mapper_registry.map_imperatively(Account, accounts_tbl)
