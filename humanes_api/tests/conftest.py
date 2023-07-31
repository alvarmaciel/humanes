import pytest
from humanes.domain.socies import Account, AccountData
from humanes.infraestructure.entity_mapping import mapper_registry
from humanes.infraestructure.repository import AccountDataRepository, AccountRepository
from sqlalchemy import create_engine, text
from sqlalchemy.orm import clear_mappers, sessionmaker


@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    mapper_registry.metadata.create_all(engine)
    return engine


@pytest.fixture
def session(in_memory_db):
    yield sessionmaker(bind=in_memory_db)()
    clear_mappers()


@pytest.fixture
def given_three_accounts_data(session) -> list[AccountData]:
    query = (
        "INSERT INTO accounts_data (name, last_name, venture, dni, zip_code, address, phone, email) VALUES "
        "('Gideon', 'Nav', '', '1234', '234', 'ninth house', '1234', 'gideon_rocks@theninth.com'), "
        "('Harrowhack', 'Nonagesimus', '', '1234', '234', 'ninth house', '1234', 'harrowhack_nonagesimuss@theninth.com'), "
        "('Ianthe', 'Thridentarus', '', '1234', '234', 'third house', '1234', 'ianthe@theninth.com')"
    )
    stmt = text(query)
    session.execute(stmt)

    repo = AccountDataRepository(session)
    retrieved = repo.list()

    return retrieved


@pytest.fixture
def given_three_accounts(given_three_accounts_data, session) -> list[AccountData]:
    accounts_data = given_three_accounts_data

    repo = AccountRepository(session)

    for account_data in accounts_data:
        account = Account(
            account_data=account_data,
            socie_type="humane",
            fees=[],
            invoices=[],
            activated=True,
            socie=True,
            provider=False,
        )
        repo.add(account)
        session.commit()

    retrieved = repo.list()

    return retrieved
