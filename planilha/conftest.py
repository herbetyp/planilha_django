import pytest
from model_bakery import baker


@pytest.fixture
def user(db, django_user_model):
    user_model = baker.make(django_user_model)
    username = 'teste'
    password = 'senha'
    user_model.set_password(password)
    user_model.username = username
    user_model.save()
    user_model.username = username
    user_model.senha = password

    return user_model


@pytest.fixture
def user_logged(user, client):
    client.force_login(user)

    return client
