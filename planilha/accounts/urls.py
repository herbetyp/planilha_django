from django.urls import path

from planilha.accounts import views

app_name = 'accounts'


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('sair/', views.logout_view, name='logout'),
    path(
        'mudar-senha/', views.CustomPasswordChangeView.as_view(), name='change-password'
    ),
]
