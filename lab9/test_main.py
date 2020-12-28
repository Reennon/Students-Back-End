import pytest

from manage import client
from manage import api
import json

# coverage run --omit 'venv/*' --omit 'test_main.py' -m pytest -q test_main.py
# coverage report --omit 'venv/*' -m

access = {}


@pytest.fixture
def login():
    print(4)
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


@pytest.fixture
def login_full_rights():
    response = client.post("/login", json=json.dumps(
        {
            "username": "test_link"
            , "password": "test_link"
        }
    ))
    access['token'] = str(response.get_data())[3:-4]
    return access['token']


@pytest.fixture
def fixture_login_post():
    return client.post("/login", json=json.dumps(
        {
            "username": "roman"
            , "password": "roman"
        }
    )).status_code


@pytest.fixture
def fixture_discipline_get(login_full_rights):
    return client.get("/disciplines", headers={
        'Authorization': 'Bearer {}'.format(login_full_rights)
    }).status_code


@pytest.fixture
def fixture_discipline_get_no_rights(login_no_rights):
    return client.get("/disciplines", headers={
        'Authorization': 'Bearer {}'.format(login_no_rights)
    }).status_code


@pytest.fixture
def fixture_discipline_post(login_full_rights):
    print(6)
    return client.post("/disciplines", headers={
        'Authorization': 'Bearer {}'.format(login_full_rights)
    }, json=json.dumps(
        {
            "DisciplineName": "Test"
            , "Credits": 4
        }
    )).status_code


@pytest.fixture
def fixture_discipline_post_no_rights(login_no_rights):
    return client.post("/disciplines", headers={
        'Authorization': 'Bearer {}'.format(login_no_rights)
    }, json=json.dumps(
        {
            "DisciplineName": "Test"
            , "Credits": 4
        }
    )).status_code


@pytest.fixture
def fixture_discipline_post_bad_data(login_full_rights):
    return client.post("/disciplines", headers={
        'Authorization': 'Bearer {}'.format(login_full_rights)
    }, json=json.dumps(
        {
            "DisciplineName": "Test"
            , "Credits": -4
        }
    )).status_code


@pytest.fixture
def fixture_discipline_put(login):
    print(7)
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


@pytest.fixture
def fixture_discipline_put_no_rights(login_no_rights):
    return client.put("/disciplines", headers={
        'Authorization': 'Bearer {}'.format(login_no_rights)
    }, json=json.dumps(
        {
            "DisciplineID": 5
            , "DisciplineName": "Information Theory"
            , "Credits": 4
        }
    )).status_code


@pytest.fixture
def fixture_discipline_put_bad_data(login_full_rights):
    return client.put("/disciplines", headers={
        'Authorization': 'Bearer {}'.format(login_full_rights)
    }, json=json.dumps(
        {
            "DisciplineID": 5
            , "DisciplineName": "Information Theory"
            , "Credits": -3
        }
    )).status_code


@pytest.fixture
def fixture_marks_get(login):
    return client.get("/marks", headers={
        'Authorization': 'Bearer {}'.format(login)
    }).status_code


@pytest.fixture
def fixture_marks_get_no_rights(login_no_rights):
    return client.get("/marks", headers={
        'Authorization': 'Bearer {}'.format(login_no_rights)
    }).status_code


@pytest.fixture
def fixture_marks_post(login_full_rights):
    return client.post("/marks", headers={
        'Authorization': 'Bearer {}'.format(login_full_rights)
    }, json=json.dumps(
        {
            "MarksID": 1
            , "DisciplineID": 1
            , "Mark": 1
            , "Passed": False
        }
    )).status_code


@pytest.fixture
def fixture_marks_post_no_rights(login_no_rights):
    return client.post("/marks", headers={
        'Authorization': 'Bearer {}'.format(login_no_rights)
    }, json=json.dumps(
        {
            "MarksID": 1
            , "DisciplineID": 1
            , "Mark": 1
            , "Passed": False
        }
    )).status_code


@pytest.fixture
def fixture_marks_post_bad_data(login_full_rights):
    return client.post("/marks", headers={
        'Authorization': 'Bearer {}'.format(login_full_rights)
    }, json=json.dumps(
        {
            "MarksID": 1
            , "DisciplineID": 1
            , "Mark": False
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

@pytest.fixture
def fixture_marks_put_no_rights(login_no_rights):
    return client.put("/marks", headers={
        'Authorization': 'Bearer {}'.format(login_no_rights)
    }, json=json.dumps(
        {
            "MarksID": 1
            , "DisciplineID": -1
            , "Mark": 1
            , "Passed": None
        }
    )).status_code

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


@pytest.fixture
def fixture_student_post(login):
    return client.post("/student", headers={
        'Authorization': 'Bearer {}'.format(login)
    }, json=json.dumps(
        {
            "Group": "Test"
            , "FirstName": "Test"
            , "LastName": "Test"
        }
    )).status_code


@pytest.fixture
def fixture_student_get():
    def _foo(login):
        return client.get("/student", headers={
            'Authorization': 'Bearer {}'.format(login)
        }, json=json.dumps(
            {
                "id": 2
            }
        )).status_code

    return _foo


@pytest.fixture()
def fixture_student_put(login):
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


def test_login_post(fixture_login_post):
    assert fixture_login_post == 200


def test_discipline_get(fixture_discipline_get, fixture_discipline_get_no_rights):
    assert fixture_discipline_get == 200
    assert fixture_discipline_get_no_rights == 405


def test_discipline_post(fixture_discipline_post, fixture_discipline_post_no_rights, fixture_discipline_post_bad_data):
    assert fixture_discipline_post == 200
    assert fixture_discipline_post_no_rights == 403
    assert fixture_discipline_post_bad_data == 405


def test_discipline_put(fixture_discipline_put, fixture_discipline_put_no_rights, fixture_discipline_put_bad_data):
    assert fixture_discipline_put == 200
    assert fixture_discipline_put_no_rights == 403
    assert fixture_discipline_put_bad_data == 405


def test_marks_get(fixture_marks_get, fixture_marks_get_no_rights):
    assert fixture_marks_get == 200
    assert fixture_marks_get_no_rights == 403


def test_marks_post(fixture_marks_post, fixture_marks_post_no_rights, fixture_marks_post_bad_data):
    assert fixture_marks_post == 200
    assert fixture_marks_post_no_rights == 405
    assert fixture_marks_post_bad_data == 403


def test_marks_put(fixture_marks_put, fixture_marks_put_bad_data, fixture_marks_put_no_rights):
    assert fixture_marks_put == 200
    assert fixture_marks_put_bad_data == 403
    assert fixture_marks_put_no_rights == 405


def test_rating_get(fixture_rating_get):
    assert fixture_rating_get == 200


def test_rating_post(fixture_rating_post):
    assert fixture_rating_post(3, 4) == 200


def test_smoke_get():
    assert client.get("/smoke").status_code == 200


def test_student_get(fixture_student_get, login, login_no_rights):
    assert fixture_student_get(login) == 200
    assert fixture_student_get(login_no_rights) == 400


def test_student_post(fixture_student_post):
    assert fixture_student_post == 200


def test_student_put(fixture_student_put):
    assert fixture_student_put(3) == 200
    assert fixture_student_put(-1) == 403
