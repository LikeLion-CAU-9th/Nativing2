from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def accounts_signup(request):
    return 


def accounts_login(request):
    return 


def accounts_logout(request):
    return 


def accounts_home(request):
    return


def signup_success(request):
    return


def login_success(request):
    return


def logout_success(request):
    return