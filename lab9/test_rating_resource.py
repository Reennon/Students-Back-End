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
def fixture_rating_post(login):
    def _foo(student_id, marks_id):
        return client.post("/rating", headers={
            'Authorization': 'Bearer {}'.format(login)
        }, json=json.dumps(
            {
                'StudentID': student_id
                , 'MarksID': marks_id
            }
        )).status_code

    return _foo


@pytest.fixture
def fixture_rating_get(login):
    return client.get("/rating", headers={
        'Authorization': 'Bearer {}'.format(login)
    }).status_code


def test_get(fixture_rating_get):
    assert fixture_rating_get == 200


def test_post(fixture_rating_post):
    assert fixture_rating_post(3, 4) == 200
