from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def accounts_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("accounts:signup_success")
            #TODO 추후 작업 후 개인 프로필로 redirect 되도록 설정 필요
        else:
            ctx = {
                "form": form,
            }
            return render(request, "accounts_signup.html", ctx)

    elif request.method == "GET":
        form = SignUpForm()
        ctx = {
            "form": form,
        }
        return render(request, "accounts_signup.html", ctx)


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