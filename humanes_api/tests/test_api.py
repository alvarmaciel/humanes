import pytest
import requests
from fastapi.testclient import TestClient

def test_api_returns_account(create_new_account, session):
    # Setup
    account = create_new_account
    import ipdb;ipdb.set_trace()
    client = TestClient(app)
    r = requests.post(f"", json=data)

    assert r.status_code == 201
    assert r.json()["batchref"] == earlybatch