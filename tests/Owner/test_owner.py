from urllib import response

import pytest
from tests.test_main import client
import json

data_correct = {
  "name": "pixal",
  "mobile": "1234567890",
  "email": "blacksheep@testmail.com",
  "password": "Shinra10sai"
}

data_incorrect = {
    "name" : "pixal",
    "mobile" : "1234567890",
    "email" : "abc@abc",
    "password" : "password"
}

owner = None

@pytest.mark.order(1)
def test_email_validation():
    response = client.post("/owner/signup", json=data_incorrect)
    assert response.status_code == 422

@pytest.mark.order(2)
def test_create_user():
    response = client.post("/owner/signup", json=data_correct)
    assert response.status_code == 201
    # d = response.json()
    d = json.loads(response.text)
    print(type(d))
    print(d)
    global owner
    owner = d
    assert "id" in d
    assert "name" in d
    assert d["name"] == data_correct["name"]
    assert "mobile" in d
    assert d["mobile"] == data_correct["mobile"]
    assert "email" in d
    assert d["email"] == data_correct["email"]
    assert "activated" in d
    assert d["activated"] == 0
    assert "created_at" in d

@pytest.mark.order(3)
def test_create_same_user():
    response = client.post("/owner/signup", json=data_correct)
    assert response.status_code == 409


@pytest.mark.order(4)
def test_user_login_without_activation():
    data = {"username" : data_correct["email"],
            "password" : data_correct["password"]}
    response = client.post("/auth/login",
                            data=data)
    print(response.text)
    assert response.status_code == 406

@pytest.mark.order(4)
def test_new_user_activation():
    with open("url.txt", "r") as fo:
        url = fo.read()
    response = client.get(url)
    assert response.status_code == 201
    d = json.loads(response.text)
    global owner
    owner = d
    assert "id" in d
    assert "name" in d
    assert d["name"] == data_correct["name"]
    assert "mobile" in d
    assert d["mobile"] == data_correct["mobile"]
    assert "email" in d
    assert d["email"] == data_correct["email"]
    assert "activated" in d
    assert d["activated"] == 1
    assert "created_at" in d

@pytest.mark.order(5)
def test_new_user_already_activated():
    with open("url.txt", "r") as fo:
        url = fo.read()
    response = client.get(url)
    assert response.status_code == 409
    print(response.text)

@pytest.mark.order(6)
def test_get_owner_by_id():
    url = f'/owner/{owner["id"]}'
    response = client.get(url)
    assert response.status_code == 200
    data = json.loads(response.text)
    assert owner == data

@pytest.mark.order(7)
def test_non_existing_owner():
    url = f'/owner/{100}'
    response = client.get(url)
    assert response.status_code == 404



    
