from sqlalchemy import text
from humanes.domain import socies


def test_account_mapper_can_load_account_data(session):  # noqa E501
    query = (
        "INSERT INTO accounts_data (name, last_name, venture, dni, zip_code, address, phone, email) VALUES "
        "('Gideon', 'Nav', '', '1234', '234', 'ninth house', '1234', 'gideon_rocks@theninth.com'), "
        "('Harrowhack', 'Nonagesimus', '', '1234', '234', 'ninth house', '1234', 'harrowhack_nonagesimuss@theninth.com'), "  # noqa E501
        "('Ianthe', 'Thridentarus', '', '1234', '234', 'third house', '1234', 'ianthe@theninth.com')"
    )
    stmt = text(query)
    session.execute(stmt)

    expected = [
        socies.AccountData("Gideon", "Nav", "", "1234", "234", "ninth house", "1234", "gideon_rocks@theninth.com"),
        socies.AccountData(
            "Harrowhack",
            "Nonagesimus",
            "",
            "1234",
            "234",
            "ninth house",
            "1234",
            "harrowhack_nonagesimuss@theninth.com",
        ),
        socies.AccountData("Ianthe", "Thridentarus", "", "1234", "234", "third house", "1234", "ianthe@theninth.com"),
    ]
    retrieved = session.query(socies.AccountData).all()

    for r, e in zip(retrieved, expected):
        assert r.name == e.name
        assert r.last_name == e.last_name
        assert r.venture == e.venture
        assert r.dni == e.dni
        assert r.zip_code == e.zip_code
        assert r.address == e.address
        assert r.phone == e.phone
        assert r.email == e.email


def test_account_mapper_can_load_account(session):
    # Setup
    query_account_data = (
        "INSERT INTO accounts_data (name, last_name, venture, dni, zip_code, address, phone, email) VALUES "
        "('Gideon', 'Nav', '', '1234', '234', 'ninth house', '1234', 'gideon_rocks@theninth.com'), "
        "('Harrowhack', 'Nonagesimus', '', '1234', '234', 'ninth house', '1234', 'harrowhack_nonagesimuss@theninth.com'), "  # noqa E501
        "('Ianthe', 'Thridentarus', '', '1234', '234', 'third house', '1234', 'ianthe@theninth.com')"
    )

    query_account = (
        "INSERT INTO accounts (account_data_id, socie_type, fees, invoices, activated, socie, provider) VALUES "
        "(1, 'humane', NULL,NULL,1, 1, 0), "
        "(2, 'adherente', NULL,NULL,1, 1, 0), "
        "(3, 'humane', NULL,NULL,1, 1, 0)"
    )

    # Exercise
    stmt_account_data = text(query_account_data)
    session.execute(stmt_account_data)

    stmt_account = text(query_account)
    session.execute(stmt_account)
    session.commit()

    # Verify
    expected_accounts_data = [
        socies.AccountData("Gideon", "Nav", "", "1234", "234", "ninth house", "1234", "gideon_rocks@theninth.com"),
        socies.AccountData(
            "Harrowhack",
            "Nonagesimus",
            "",
            "1234",
            "234",
            "ninth house",
            "1234",
            "harrowhack_nonagesimuss@theninth.com",
        ),
        socies.AccountData("Ianthe", "Thridentarus", "", "1234", "234", "third house", "1234", "ianthe@theninth.com"),
    ]
    accounts_data = session.query(socies.AccountData).all()
    assert accounts_data == expected_accounts_data

    expected_accounts = [
        socies.Account(expected_accounts_data[0], "humane", None, None, 1, 1, 0),
        socies.Account(expected_accounts_data[1], "adherente", None, None, 1, 1, 0),
        socies.Account(expected_accounts_data[2], "humane", None, None, 1, 1, 0),
    ]
    retrived_accounts = session.query(socies.Account).all()
    for r, e in zip(retrived_accounts, expected_accounts):
        assert r.account_data == e.account_data
        assert r.socie_type == e.socie_type
        assert r.fees == e.fees
        assert r.invoices == e.invoices
        assert r.activated == e.activated
        assert r.socie == e.socie
        assert r.provider == e.provider
