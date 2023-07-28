import random
import string

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import clear_mappers, sessionmaker

from humanes_api.humanes.domain.socies import Account, AccountData
from humanes_api.humanes.infraestructure.entity_mapping import mapper_registry, start_mappers


@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    mapper_registry.metadata.create_all(engine)
    return engine


@pytest.fixture
def session(in_memory_db):
    start_mappers()
    yield sessionmaker(bind=in_memory_db)()
    clear_mappers()


@pytest.fixture
def create_new_account(
    type: str = "adherente",
    activated: bool = True,
) -> Account:
    import ipdb

    ipdb.set_trace()
    insert_account_data = (
        "INSERT INTO accounts_data (name, last_name, venture, dni, zip_code, address, phone, email) VALUES "
        "('Gideon', 'Nav', '', '1234', '234', 'ninth house', '1234', 'gideon_rocks@theninth.com'), "
        "('Harrowhack', 'Nonagesimus', '', '12345', '234', 'ninth house', '1235', 'harrowhack_nonagesimuss@theninth.com'), "
        "('Ianthe', 'Thridentarus', '', '12346', '234', 'third house', '2234', 'ianthe@theninth.com')"
    )
    stmt = text(insert_account_data)
    session.execute(stmt)
    insert_account = "INSERT INTO accounts ()"
    # Account(account_data=account_data, socie_type=type, activated=activated)

    return account
