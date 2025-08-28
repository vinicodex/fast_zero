from http import HTTPStatus


def test_read_root(client):
    response = client.get('/')
    assert response.json() == {'message': 'Olá, Mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'string2',
            'email': 'user@example.com',
            'password': 'string',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'string2',
        'email': 'user@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'string2',
                'email': 'user@example.com',
                'id': 1,
            }
        ]
    }


def test_should_raise_exception(client):
    response = client.put(
        '/users/0',
        json={
            'username': 'Marcos',
            'email': 'marcos@example.com',
            'password': 'marcos',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Marcos',
            'email': 'marcos@example.com',
            'password': 'marcos',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Marcos',
        'email': 'marcos@example.com',
        'id': 1,
    }


def test_should_raise_exception_when_deleting_user(client):
    response = client.delete(
        '/users/0',
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
