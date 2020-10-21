from django.urls import path

from planilha.accounts import views

app_name = 'accounts'


urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
