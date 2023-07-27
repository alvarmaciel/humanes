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
