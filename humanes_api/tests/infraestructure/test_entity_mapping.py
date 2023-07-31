from sqlalchemy import text

from humanes_api.humanes.domain import socies


def test_account_mapper_can_load_account_data(session):
    query = "INSERT INTO accounts_data (name, last_name, venture, dni, zip_code, address, phone, email) VALUES " \
            "('Gideon', 'Nav', '', '1234', '234', 'ninth house', '1234', 'gideon_rocks@theninth.com'), " \
            "('Harrowhack', 'Nonagesimus', '', '1234', '234', 'ninth house', '1234', 'harrowhack_nonagesimuss@theninth.com'), " \
            "('Ianthe', 'Thridentarus', '', '1234', '234', 'third house', '1234', 'ianthe@theninth.com')"
    stmt = text(query)
    session.execute(stmt)

    expected = [
        socies.AccountData("Gideon", "Nav", "", "1234", "234", "ninth house", "1234", "gideon_rocks@theninth.com"),
        socies.AccountData("Harrowhack", "Nonagesimus", "", "1234", "234", "ninth house", "1234",
                           "harrowhack_nonagesimuss@theninth.com"),
        socies.AccountData('Ianthe', 'Thridentarus', '', '1234', '234', 'third house', '1234', 'ianthe@theninth.com'),
    ]
    assert session.query(socies.AccountData).all() == expected


def test_account_mapper_can_load_account(session):
    # Setup
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

    # Exercise
    stmt_account_data = text(query_account_data)
    session.execute(stmt_account_data)

    stmt_account = text(query_account)
    session.execute(stmt_account)

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
        socies.Account(expected_accounts_data[0], "humane", "", "", 1, 1, 0),
        socies.Account(expected_accounts_data[1], "adherente", "", "", 1, 1, 0),
        socies.Account(expected_accounts_data[2], "humane", "", "", 1, 1, 0),
    ]

    assert session.query(socies.Account).all() == expected_accounts
