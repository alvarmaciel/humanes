import settings
from humanes.domain.socies import Account, AccountData
from humanes.infraestructure.database import DATABASE_URL, SessionLocal
from sqlalchemy import create_engine


def populate_database():
    engine = create_engine(DATABASE_URL)
    with SessionLocal() as session:
        # Check if the database is already populated
        existing_account_data = session.query(AccountData).all()
        if existing_account_data:
            print("Database already populated. Skipping data insertion.")
            return

        # Add the logic here to populate the database with the provided data
        expected_accounts_data = [
            AccountData("Gideon", "Nav", "", "1234", "234", "ninth house", "1234", "gideon_rocks@theninth.com"),
            AccountData(
                "Harrowhack",
                "Nonagesimus",
                "",
                "1234",
                "234",
                "ninth house",
                "1234",
                "harrowhack_nonagesimuss@theninth.com",
            ),
            AccountData("Ianthe", "Thridentarus", "", "1234", "234", "third house", "1234", "ianthe@theninth.com"),
        ]
        for account_data in expected_accounts_data:
            session.add(account_data)
        session.commit()

        expected_accounts = [
            Account(expected_accounts_data[0], "humane", None, None, 1, 1, 0),
            Account(expected_accounts_data[1], "adherente", None, None, 1, 1, 0),
            Account(expected_accounts_data[2], "humane", None, None, 1, 1, 0),
        ]
        for account in expected_accounts:
            session.add(account)
        session.commit()


if __name__ == "__main__":
    populate_database()
