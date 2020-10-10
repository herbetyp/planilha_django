import pytest
from django.urls import reverse
from model_bakery import baker

from planilha.core.models import Spent
from planilha.django_assertions import assert_contains


@pytest.fixture
def spent(db):
    return baker.make(Spent)


@pytest.fixture
def resp_get(client, spent):
    return client.get(reverse('core:home'))


def test_status_code(resp_get):
    assert resp_get.status_code == 200


def test_title(resp_get):
    assert_contains(resp_get, '<title>Home</title>')


def test_home_link_navbar(resp_get):
    assert_contains(resp_get, f'href="{reverse("core:home")}">Home</a>')
