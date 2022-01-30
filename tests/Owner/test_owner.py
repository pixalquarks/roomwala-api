from tests.test_main import client
import json

data = {
  "name": "pixal",
  "mobile": "1234567890",
  "email": "hit19ece112.rakshat@gmail.com",
  "password": "Shinra10sai"
}

def test_create_user():
    response = client.post("/owner/signup", json=data)
    assert response.status_code == 201
    # d = response.json()
    d = json.loads(response.text)
    print(type(d))
    print(d)
    assert d["name"] == data["name"]
    assert d["mobile"] == data["mobile"]
    assert d["email"] == data["email"]
    assert d["activated"] == 0
    
