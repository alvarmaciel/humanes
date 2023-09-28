import pytest
from fastapi.testclient import TestClient
from humanes.app import app
from humanes.domain.socies import Account, AccountData
from humanes.infraestructure.repository import AccountDataRepository, AccountRepository


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
    for account_data in [account_data_1, account_data_2, account_data_3]:
        repo.add(account_data)
    session.commit()
    return [account_data_1, account_data_2, account_data_3]


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
        accounts.append(account)

    session.commit()
    retrieved = repo.list()

    return retrieved
def test_api_returns_account(given_three_accounts, session):
    """
    Given three accounts
    When I hit the endpoint /socies/
    Then I get a list with three accounts
    """
    # Setup: Create three accounts
    client = TestClient(app)
    repo = AccountRepository(session)
    # Exercise
    response = client.get("/socies/")
    # Verify
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json() == expected_accounts()


def test_api_get_status_deactivatred_account(given_three_accounts, session):
    """
    Given three accounts
    When I hit the endpoint /socies/get_status/1
    Then I get the account with id 1
    """
    # Setup: Create three accounts
    client = TestClient(app)
    # Exercise
    response = client.get("/socies/get_status/1")
    # Verify
    expected = {
        "account_data": {
            "name": "Gideon",
            "last_name": "Nav",
            "venture": "",
            "dni": "1234",
            "zip_code": "234",
            "address": "ninth house",
            "phone": "1234",
            "email": "gideon_rocks@theninth.com",
        },
        "socie_type": "humane",
        "fees": None,
        "invoices": None,
        "activated": False,
        "socie": True,
        "provider": False,
    }
    assert response.status_code == 200
    assert response.json() == expected

    # # Setup: Create three accounts
    # client = TestClient(app)
    # # # Exercise
    # response = client.get(f"/socies/get_status/{accounts[0].id}")
    # # # Verify
    # expected = {
    #     "account_data": {
    #         "name": "Gideon",
    #         "last_name": "Nav",
    #         "venture": "",
    #         "dni": "1234",
    #         "zip_code": "234",
    #         "address": "ninth house",
    #         "phone": "1234",
    #         "email": "gideon_rocks@theninth.com",
    #     },
    #     "socie_type": "humane",
    #     "fees": None,
    #     "invoices": None,
    #     "activated": False,
    #     "socie": True,
    #     "provider": False,
    # }
    # assert response.status_code == 200
    # assert response.json() == expected

def expected_accounts():
    return [
        {
            "account_data": {
                "name": "Gideon",
                "last_name": "Nav",
                "venture": "",
                "dni": "1234",
                "zip_code": "234",
                "address": "ninth house",
                "phone": "1234",
                "email": "gideon_rocks@theninth.com",
            },
            "socie_type": "humane",
            "fees": None,
            "invoices": None,
            "activated": True,
            "socie": True,
            "provider": False,
        },
        {
            "account_data": {
                "name": "Harrowhack",
                "last_name": "Nonagesimus",
                "venture": "",
                "dni": "1234",
                "zip_code": "234",
                "address": "ninth house",
                "phone": "1234",
                "email": "harrowhack_nonagesimuss@theninth.com",
            },
            "socie_type": "adherente",
            "fees": None,
            "invoices": None,
            "activated": True,
            "socie": True,
            "provider": False,
        },
        {
            "account_data": {
                "name": "Ianthe",
                "last_name": "Thridentarus",
                "venture": "",
                "dni": "1234",
                "zip_code": "234",
                "address": "third house",
                "phone": "1234",
                "email": "ianthe@theninth.com",
            },
            "socie_type": "humane",
            "fees": None,
            "invoices": None,
            "activated": True,
            "socie": True,
            "provider": False,
        },
    ]
