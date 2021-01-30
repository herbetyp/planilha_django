# import pytest
# from django.urls import reverse
# from model_bakery import baker

# from planilha.core.models import Spent
# from planilha.django_assertions import assert_in


# @pytest.fixture
# def spent(db, user):
#     return baker.make(Spent, user=user, spent='Teste')


# @pytest.fixture
# def resp_post_create(user_logged, user):
#     data = {'spent': 'teste_create', 'date': '2020-10-04', 'value': '200'}
#     return user_logged.post(
#         reverse("core:create", kwargs={'month': 'Janeiro', 'year': '2020'}),
#         data=data,
#         user=user,
#     )


# @pytest.fixture
# def resp_post_update(user_logged, spent):
#     data = {
#         'spent': 'teste_update',
#         'date': '2020-10-05',
#         'value': '250',
#         'fixed_account': True,
#     }
#     return user_logged.post(
#         reverse(
#             "core:update", kwargs={'pk': spent.pk, 'month': 'Fevereiro', 'year': '2020'}
#         ),
#         data=data,
#     )


# @pytest.fixture
# def resp_post_error_fields_white(user_logged, spent):
#     data = {'spent': '', 'date': '', 'value': ''}
#     return user_logged.post(
#         reverse(
#             "core:update", kwargs={'pk': spent.pk, 'month': 'Abril', 'year': '2020'}
#         ),
#         data=data,
#     )


# @pytest.fixture
# def resp_post_error_date_invalid(user_logged, spent):
#     data = {'spent': 'test', 'date': '01-05', 'value': '10'}
#     return user_logged.post(
#         reverse("core:update", kwargs={'pk': spent.pk, 'month': 'Maio', 'year': '2020'}),
#         data=data,
#     )


# @pytest.fixture
# def resp_post_delete(user_logged, spent):
#     return user_logged.post(
#         reverse("core:delete", kwargs={'pk': spent.pk, 'month': 'Junho'})
#     )


# @pytest.fixture
# def resp_get_update(user_logged, resp_post_update, spent):
#     return user_logged.get(
#         reverse("core:update", kwargs={'pk': spent.pk, 'month': 'Marco', 'year': '2020'})
#     )


# def test_create_spent(resp_post_create):
#     assert resp_post_create.status_code == 200
#     assert resp_post_create.json().get('url') == reverse(
#         "core:month", kwargs={'month': 'Janeiro'}
#     )


# def test_update_spent_post(resp_post_update):
#     assert resp_post_update.status_code == 200
#     assert resp_post_update.json().get('url') == reverse(
#         "core:month", kwargs={'month': 'Fevereiro'}
#     )


# def test_update_spent_get(resp_get_update):
#     assert resp_get_update.status_code == 200
#     resp = resp_get_update.json()
#     assert resp == {
#         'date': '2020-10-05',
#         'spent': 'teste_update',
#         'value': '250.00',
#         'fixed_account': True,
#     }


# def test_update_spent_error_fields_white(resp_post_error_fields_white):
#     assert resp_post_error_fields_white.status_code == 400
#     errors = resp_post_error_fields_white.json().get('errors')
#     for error in errors.values():
#         assert error == ['Este campo é obrigatório.']


# def test_update_spent_error_date_invalid(resp_post_error_date_invalid):
#     assert resp_post_error_date_invalid.status_code == 400
#     errors = resp_post_error_date_invalid.json().get('errors')
#     assert_in(['Informe uma data válida.'], errors.values())


# def test_delete_spent(resp_post_delete):
#     assert resp_post_delete.status_code == 200
#     assert resp_post_delete.json().get('url') == reverse(
#         "core:month", kwargs={'month': 'Junho'}
#     )
