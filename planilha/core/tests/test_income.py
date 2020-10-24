import pytest
from django.urls import reverse
from model_bakery import baker

from planilha.core.models import Income


@pytest.fixture
def income(db, user):
    return baker.make(Income, user=user)


@pytest.fixture
def resp_post_income_update(user_logged, income):
    data = {'income': '500', 'save_percent': '5'}
    return user_logged.post(reverse("core:income"), data=data)


@pytest.fixture
def resp_post_income_create(user_logged, income):
    data = {'income': '400', 'save_percent': '10'}
    return user_logged.post(reverse("core:income"), data=data)


def test_income_post_update(resp_post_income_update):
    assert resp_post_income_update.status_code == 200
    assert resp_post_income_update.json().get('url') == reverse("core:home")


def test_income_post_create(resp_post_income_create):
    assert resp_post_income_create.status_code == 200
    assert resp_post_income_create.json().get('url') == reverse("core:home")
