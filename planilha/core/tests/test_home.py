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


def test_btn_add_spent(resp):
    assert_contains(
        resp, '<a class="btn btn-primary btn-sm float-right" href="#">Adicionar</a>'
    )


def test_btn_update_spent(resp):
    assert_contains(resp, '<a class="btn btn-warning btn-sm" href="#">Alterar</a>')


def test_btn_remove_spent(resp):
    assert_contains(
        resp, '<a class="btn btn-danger btn-sm ml-1 text-white" href="#">Excluir</a>'
    )
