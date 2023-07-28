from datetime import date

from sqlalchemy import text

from humanes_api.humanes.domain.socies import AccountData, Account
from humanes_api.humanes.infraestructure import repository


def insert_account_data(session):
    insert = "INSERT INTO accounts_data (name, last_name, venture, dni, zip_code, address, phone, email) VALUES " \
             "('Gideon', 'Nav', '', '1234', '234', 'ninth house', '1234', 'gideon_rocks@theninth.com'), " \
             "('Harrowhack', 'Nonagesimus', '', '12345', '234', 'ninth house', '1235', 'harrowhack_nonagesimuss@theninth.com'), " \
             "('Ianthe', 'Thridentarus', '', '12346', '234', 'third house', '2234', 'ianthe@theninth.com')"
    stmt = text(insert)
    session.execute(stmt)
    query = text("SELECT id FROM accounts_data")
    accounts_data_id = session.execute(query).fetchall()
    return accounts_data_id


def test_repository_can_save_an_account_data(session):
    # Setup
    account_data = AccountData("a name", "a last name", "", "123456", "1245", "an address", "+5468", "an email")

    # Exercise
    repo = repository.AccountDataRepository(session)
    repo.add(account_data)
    session.commit()

    # Verify
    query = text("SELECT name, last_name, venture, dni FROM 'accounts_data'")
    results = session.execute(query).fetchall()
    assert results == [("a name", "a last name", "", "123456")]


def test_repository_can_get_saved_account_data(session):
    # Setup
    import ipdb;ipdb.set_trace()

    accounts_data_id=insert_account_data(session)
    reference = '1234'

    # Exercise
    repo = repository.AccountDataRepository(session)
    retrieved = repo.get(reference)

    # Verify
    expected = AccountData(name='Gideon', last_name='Nav', venture='', dni='1234', zip_code='234',
                           address='ninth house', phone='1234', email='gideon_rocks@theninth.com')
    assert retrieved == expected


def test_repository_can_list_saved_account_data(session):
    # Setup
    accounts_data = insert_account_data(session)
    # Exercise
    repo = repository.AccountDataRepository(session)
    retrieved = repo.list()

    # Verify
    assert len(retrieved) == len(accounts_data)


def test_repository_can_save_an_account(session):
    # Setup
    account_data = AccountData("a name", "a last name", "", "123456", "1245", "an address", "+5468", "an email")
    fees = [
        {"date": date(2022, 1, 1), "amount": 100},
        {"date": date(2022, 2, 1), "amount": 100},
        {"date": date(2022, 2, 1), "amount": 100}
    ]
    account = Account(account_data=account_data, socie_type="humane", fees=fees, invoices=[], activated=True,
                      socie=True, provider=False)
    # Exercise
    repo_account_data = repository.AccountDataRepository(session)
    repo_account_data.add(account_data)
    repo_account = repository.AccountRepository(session)
    session.commit()

    # Verify
    import ipdb;ipdb.set_trace()
    query_account_data = text("SELECT name, last_name, venture, dni FROM 'accounts_data'")
    results_account_data = session.execute(query_account_data).fetchall()
    query_account = text("SELECT name, last_name, venture, dni FROM 'accounts_data'")
    results_account = session.execute(query_account).fetchall()
    assert results_account_data == [("a name", "a last name", "", "123456")]


def test_repository_can_get_saved_account(session):
    # Setup
    insert_account_data(session)
    reference = '1234'

    # Exercise
    repo = repository.AccountDataRepository(session)
    retrieved = repo.get(reference)

    # Verify
    expected = AccountData(name='Gideon', last_name='Nav', venture='', dni='1234', zip_code='234',
                           address='ninth house', phone='1234', email='gideon_rocks@theninth.com')
    assert retrieved == expected


def test_repository_can_list_saved_account(session):
    # Setup
    accounts_data = insert_account_data(session)
    # Exercise
    repo = repository.AccountDataRepository(session)
    retrieved = repo.list()

    # Verify
    assert len(retrieved) == len(accounts_data)
