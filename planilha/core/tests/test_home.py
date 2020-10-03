import pytest
from django.urls import reverse

from planilha.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('core:home'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Home</title>')
