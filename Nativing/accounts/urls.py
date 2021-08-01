from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', accounts_home, name="accounts_home"),
    path('signup/', accounts_signup, name='accounts_signup'),
    path('login/', accounts_login, name="accounts_login"),
    path('logout/', accounts_logout, name="accounts_logout"),
    path("signup_success/", signup_success, name='signup_success'),
    path("login_success/", login_success, name="login_success"),
    path("logout_success/", logout_success, name="logout_success"),
]
