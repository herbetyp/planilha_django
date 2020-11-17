import pytest
from django.urls import reverse
from model_bakery import baker

from planilha.core.models import Income
from planilha.django_assertions import assert_contains


@pytest.fixture
def income(db, user):
    return baker.make(Income, user=user)


@pytest.fixture
def resp_get(user_logged, income):
    return user_logged.get(reverse('accounts:change-password'))


@pytest.fixture
def resp_post(user_logged, income):
    data = {
        'old_password': 'senha',
        'new_password1': '123456',
        'new_password2': '123456',
    }
    return user_logged.post(reverse('accounts:change-password'), data=data)


@pytest.fixture
def resp_get_register(client):
    return client.get(reverse('accounts:register'))


@pytest.fixture
def resp_post_register(client, db):
    data = {
        'username': 'teste',
        'email': 'teste@email.com',
        'password': 'teste01',
        'password2': 'teste01',
    }
    return client.post(reverse('accounts:register'), data=data)


def test_status_code(resp_get):
    assert resp_get.status_code == 200


def test_post_link_change_password(resp_get):
    assert_contains(resp_get, reverse('accounts:change-password'))


def test_post_change_password(resp_post):
    assert resp_post.status_code == 302


def test_status_code_register(resp_get_register):
    assert resp_get_register.status_code == 200


def test_register_form_valid(resp_post_register):
    assert resp_post_register.status_code == 302
