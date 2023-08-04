import pytest
from humanes_api.humanes.domain.socies import Account, AccountData
from humanes_api.humanes.infraestructure.entity_mapping import mapper_registry
from humanes_api.humanes.infraestructure.repository import AccountDataRepository, AccountRepository
from sqlalchemy import create_engine, text
from sqlalchemy.orm import clear_mappers, sessionmaker


@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    mapper_registry.metadata.create_all(engine)
    return engine


@pytest.fixture
def session(in_memory_db):
    session = sessionmaker(bind=in_memory_db)()
    yield session
    clear_mappers()
    session.close()


@pytest.fixture
def given_three_accounts_data(session) -> list[AccountData]:
    account_data_1 = AccountData(
        "Gideon", "Nav", "", "123456", "1245", "ninth house", "+5468", "gideon_rocks@theninth.com"
    )
    account_data_2 = AccountData(
        "Harrowhack", "Nonagesimus", "", "1234", "234", "ninth house", "1234", "harrowhack_nonagesimuss@theninth.com"
    )
    account_data_3 = AccountData(
        "Ianthe", "Thridentarus", "", "1234", "234", "third house", "1234", "ianthe@theninth.com"
    )
    repo = AccountDataRepository(session)
    repo.add(account_data_1)
    repo.add(account_data_2)
    repo.add(account_data_3)
    session.commit()

    retrieved = repo.list()

    return retrieved


@pytest.fixture
def given_three_accounts(given_three_accounts_data, session) -> list[AccountData]:
    accounts_data = given_three_accounts_data

    repo = AccountRepository(session)
    accounts = []
    for account_data in accounts_data:
        account = Account(
            account_data=account_data,
            socie_type="humane",
            fees=None,
            invoices=None,
            activated=True,
            socie=True,
            provider=False,
        )
        repo.add(account)
        session.commit()
        accounts.append(account)

    retrieved = repo.list()

    return retrieved
