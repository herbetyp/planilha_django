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


def test_status_code(resp_get):
    assert resp_get.status_code == 200


def test_post_link_change_password(resp_get):
    assert_contains(resp_get, reverse('accounts:change-password'))


def test_post_change_password(resp_post):
    assert resp_post.status_code == 302
