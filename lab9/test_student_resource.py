import pytest

from manage import client
import json

access = {}


@pytest.fixture
def login():
    response = client.post("/login", json=json.dumps(
        {
            "username": "roman"
            , "password": "roman"
        }
    ))
    access['token'] = str(response.get_data())[3:-4]
    return access['token']

@pytest.fixture
def login_no_rights():
    response = client.post("/login", json=json.dumps(
        {
            "username": "test"
            , "password": "test"
        }
    ))
    access['token'] = str(response.get_data())[3:-4]
    return access['token']


def test_get(login, login_no_rights):
    assert client.get("/student", headers={
        'Authorization': 'Bearer {}'.format(login)
    }, json=json.dumps(
        {
            "id": 2
        }
    )).status_code == 200
    assert client.get("/student", headers={
        'Authorization': 'Bearer {}'.format(login_no_rights)
    }, json=json.dumps(
        {
            "id": 2
        }
    )).status_code == 400
    """
    
    """


def test_post(login):
    assert client.post("/student", headers={
        'Authorization': 'Bearer {}'.format(login)
    }, json=json.dumps(
        {
            "Group": "Test"
            , "FirstName": "Test"
            , "LastName": "Test"
        }
    )).status_code == 200


@pytest.fixture()
def student_put(login):
    def _foo(id):
        return client.put("/student", headers={
            'Authorization': 'Bearer {}'.format(login)
        }, json=json.dumps(
            {
                "id": id
                , "Group": "Test"
                , "FirstName": "Test"
                , "LastName": "Test"
            }
        )).status_code
    return _foo

def test_put(student_put):
    assert student_put(3) == 200
    assert student_put(-1) == 403

