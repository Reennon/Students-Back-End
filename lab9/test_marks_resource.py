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
def fixture_marks_get(login):
    return client.get("/marks", headers={
        'Authorization': 'Bearer {}'.format(login)
    }).status_code


@pytest.fixture
def fixture_marks_post(login):
    return client.post("/marks", headers={
        'Authorization': 'Bearer {}'.format(login)
    }, json=json.dumps(
        {
            "MarksID": 1
            , "DisciplineID": 1
            , "Mark": 1
            , "Passed": False
        }
    )).status_code


@pytest.fixture
def fixture_marks_put(login):
    return client.put("/marks", headers={
        'Authorization': 'Bearer {}'.format(login)
    }, json=json.dumps(
        {
            "MarksID": 1
            , "DisciplineID": 1
            , "Mark": 1
            , "Passed": False
        }
    )).status_code


@pytest.fixture
def fixture_marks_put_bad_data(login):
    return client.put("/marks", headers={
        'Authorization': 'Bearer {}'.format(login)
    }, json=json.dumps(
        {
            "MarksID": 1
            , "DisciplineID": -1
            , "Mark": 1
            , "Passed": None
        }
    )).status_code


def test_get(fixture_marks_get):
    assert fixture_marks_get == 200


def test_post(fixture_marks_post):
    assert fixture_marks_post == 200


def test_put(fixture_marks_put, fixture_marks_put_bad_data):
    assert fixture_marks_put == 200
    assert fixture_marks_put_bad_data == 403
