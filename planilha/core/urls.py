from django.urls import path

from planilha.core import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('deletar/<int:pk>', views.delete_spent_view, name='delete'),
    path('alterar/<int:pk>', views.update_spent_view, name='update'),
    path('adicionar/', views.create_spent_view, name='create'),
    path('renda/', views.income_view, name='income'),
]
