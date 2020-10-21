import pytest
from django.urls import reverse


@pytest.fixture
def resp_get_login(client):
    return client.get(reverse('accounts:login'))


@pytest.fixture
def resp_get_logout(user_logged):
    return user_logged.get(reverse('accounts:logout'))


@pytest.fixture
def resp_post_login(client, user):
    return client.post(
        reverse('accounts:login'), {'username': user.username, 'password': user.senha}
    )


@pytest.fixture
def resp_post_login_error_redirect(client, user):
    return client.post(
        reverse('accounts:login'), {'username': 'teste_error', 'password': user.senha}
    )


def test_status_code_login(resp_get_login):
    assert resp_get_login.status_code == 200


def test_logout_redirect(resp_get_logout):
    assert resp_get_logout.status_code == 302
    assert resp_get_logout.url == reverse('accounts:login')


def test_login_redirect(resp_post_login):
    assert resp_post_login.status_code == 302
    assert resp_post_login.url == reverse('core:home')


def test_login_error_redirect(resp_post_login_error_redirect):
    assert resp_post_login_error_redirect.url == reverse('accounts:login')
