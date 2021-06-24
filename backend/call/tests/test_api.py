from http import HTTPStatus

import pytest


@pytest.mark.django_db
def test_create_call(client, call):
    url = '/api/v1/call/calls'
    response = client.post(url, call, content_type='application/json')
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_list_calls_status_code(client):
    url = '/api/v1/call/calls'
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_update_call(client, call):
    url = '/api/v1/call/calls'
    client.post(url, call, content_type='application/json')

    url = '/api/v1/call/calls/1'
    response = client.put(url, call, content_type='application/json')
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_delete_call(client, call):
    url = '/api/v1/call/calls'
    client.post(url, call, content_type='application/json')

    url = '/api/v1/call/calls/1'
    response = client.delete(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_delete_call_response(client, call):
    url = '/api/v1/call/calls'
    client.post(url, call, content_type='application/json')

    url = '/api/v1/call/calls/1'
    response = client.delete(url)
    assert response.json() == {"success": True}
