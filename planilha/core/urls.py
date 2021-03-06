from django.urls import path

from planilha.core import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('deletar/<int:pk>/<str:month>', views.delete_spent_view, name='delete'),
    path(
        'alterar/<int:pk>/<str:month>/<int:year>',
        views.update_spent_view,
        name='update',
    ),
    path('adicionar/<str:month>/<int:year>', views.create_spent_view, name='create'),
    path('renda/<str:month>/<int:year>', views.income_view, name='income'),
    path('mes/<str:month>/', views.month_view, name='month'),
]
