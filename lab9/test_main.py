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
def fixture_discipline_get(login):
    return client.get("/rating", headers={
        'Authorization': 'Bearer {}'.format(login)
    }).status_code


@pytest.fixture
def fixture_discipline_post(login):
    return client.post("/disciplines", headers={
        'Authorization': 'Bearer {}'.format(login)
    }, json=json.dumps(
        {
            "DisciplineName": "Test"
            , "Credits": 4
        }
    )).status_code


@pytest.fixture
def fixture_discipline_put(login):
    # fixture_discipline_post
    return client.put("/disciplines", headers={
        'Authorization': 'Bearer {}'.format(login)
    }, json=json.dumps(
        {
            "DisciplineID": 5
            , "DisciplineName": "Information Theory"
            , "Credits": 4
        }
    )).status_code


def test_discipline_get(fixture_discipline_get):
    assert fixture_discipline_get == 200


def test_discipline_post(fixture_discipline_post):
    assert fixture_discipline_post == 200


def test_discipline_put(fixture_discipline_put):
    assert fixture_discipline_put == 200
