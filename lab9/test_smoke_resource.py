from manage import client


def test_get():
    assert client.get("/smoke").status_code == 200
