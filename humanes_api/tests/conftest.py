import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import clear_mappers, sessionmaker
import settings
from humanes.infraestructure.entity_mapping import mapper_registry

@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    mapper_registry.metadata.create_all(engine)
    return engine


@pytest.fixture
def session(in_memory_db):
    SessionLocal = sessionmaker(bind=in_memory_db)()
    session = SessionLocal

    yield session
    session.close()
    # clear_mappers()
    # in_memory_db.dispose()

@pytest.fixture
def add_accounts(session):
    query_account_data = (
        "INSERT INTO accounts_data (name, last_name, venture, dni, zip_code, address, phone, email) VALUES "
        "('Gideon', 'Nav', '', '1234', '234', 'ninth house', '1234', 'gideon_rocks@theninth.com'), "
        "('Harrowhack', 'Nonagesimus', '', '1234', '234', 'ninth house', '1234', 'harrowhack_nonagesimuss@theninth.com'), "
        "('Ianthe', 'Thridentarus', '', '1234', '234', 'third house', '1234', 'ianthe@theninth.com')"
    )

    query_account = (
        "INSERT INTO accounts (account_data_id, socie_type, fees, invoices, activated, socie, provider) VALUES "
        "(1, 'humane', '','',1, 1, 0), "
        "(2, 'adherente', '','',1, 1, 0), "
        "(3, 'humane', '','',1, 1, 0)"
    )

    stmt_account_data = text(query_account_data)
    session.execute(stmt_account_data)

    stmt_account = text(query_account)
    session.execute(stmt_account)

    session.commit()

