from manage import client
import json


def test_post():
    assert client.post("/login", json=json.dumps(
        {
            "username": "roman"
            , "password": "roman"
        }
    )).status_code == 200


'''
    assert client.post("/login", json=json.dumps(
        {
            "username": "roman"
            , "password": "roman"
        }
    )).status_code == 200
'''
