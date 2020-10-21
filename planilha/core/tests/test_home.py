import pytest
from django.urls import reverse
from model_bakery import baker

from planilha.core.models import Income
from planilha.core.models import Spent
from planilha.django_assertions import assert_contains
from planilha.django_assertions import assert_not_contains


@pytest.fixture
def spent(db, user):
    return baker.make(Spent, user=user, value='10')


@pytest.fixture
def income(db, user):
    return baker.make(Income, user=user)


@pytest.fixture
def resp_home_logged(user_logged, spent, income):
    return user_logged.get(reverse('core:home'))


@pytest.fixture
def resp_home_not_logged(client, spent, income):
    return client.get(reverse('core:home'))


# Deslogado
def test_status_code_not_logged(resp_home_not_logged):
    assert resp_home_not_logged.status_code == 302
    assert reverse('accounts:login')


# Logado
def test_status_code_logged(resp_home_logged):
    assert resp_home_logged.status_code == 200


def test_title_logged(resp_home_logged):
    assert resp_home_logged.status_code == 200
    assert_contains(resp_home_logged, '<title>Planilha - Home</title>')


def test_home_link_navbar_logged(resp_home_logged):
    assert resp_home_logged.status_code == 200
    assert_not_contains(resp_home_logged, f'href="{reverse("core:home")}">Home</a>')


def test_exit_link_navbar_logged(resp_home_logged):
    assert resp_home_logged.status_code == 200
    assert_not_contains(
        resp_home_logged, f'href="{reverse("accounts:logout")}">Sair</a> '
    )


def test_user_logged(resp_home_logged, user):
    assert_contains(resp_home_logged, user.username)
