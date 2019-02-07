from flask import url_for


def test_hello_service(client):
    res = client.get(url_for('hello_world'))
    assert res.status_code == 200
