from fastapi.testclient import TestClient
from humanes_api.humanes.app import app


def test_api_returns_account(given_three_accounts, session):
    # Setup
    accounts = given_three_accounts
    assert len(accounts) == 3
    client = TestClient(app)
    # Excrcise
    response = client.get("/socies/")
    # Verify
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json() == expected_accounts()


def test_api_returns_400_if_no_data():
    client = TestClient(app)
    # Excrcise
    response = client.get("/socies")
    # Verify
    assert response.status_code == 404
    assert response.json() == {"detail": "Socies not found"}


def test_api_get_status_deactivated(given_three_accounts, session):
    # Setup
    accounts = given_three_accounts
    assert len(accounts) == 3
    client = TestClient(app)
    # # Exercise
    # response = client.get(f"/socies/get_status/{accounts[0].id}")
    # # Verify
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
