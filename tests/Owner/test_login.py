from urllib import response
from tests.Owner.test_owner import owner, data_correct
from tests.test_main import client

import pytest
import json


# def test_emailverification_login_route():
#     data = {"username" : "blablabla@abc",
#             "password" : "password"}
#     response = client.post("/auth/login", data=data)
#     assert response.status_code == 422


def test_nonexisting_owner_login():
    data = {"username" : "blablabla@abc.com",
            "password" : "password"}
    response = client.post("/auth/login", data=data)
    assert response.status_code == 403

@pytest.mark.order(8)
def test_wrong_password():
    data = {"username" : data_correct["email"],
            "password" : "password"}
    response = client.post("/auth/login", data=data)
    assert response.status_code == 403

@pytest.mark.order(9)
def test_login():
    data = {"username" : data_correct["email"],
            "password" : data_correct["password"]}
    response = client.post("/auth/login", data=data)
    assert response.status_code == 202
    d = json.loads(response.text)
    assert "access_token" in d
    assert "token_type" in d
    assert d["token_type"] == "bearer"

        
