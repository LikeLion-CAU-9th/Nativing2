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
            #TODO 추후 회원가입 후 개인 프로필로 redirect 되도록 설정 필요
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
    if request.method == "POST":
        form = LoginForm(request.POST)
        email = request.POST.get("email")
        password = request.POST["password"]
        user = authenticate(email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("accounts:login_success")
            #TODO 추후 로그인 후 개인 프로필로 redirect 되도록 설정 필요
        else:
            ctx = {
                "form": form,
                "error": "email or password is incorrect",
            }
            return render(request, "accounts_login.html", ctx)
    elif request.method == "GET":
        form = LoginForm()
        ctx = {
            "form": form,
        }
        return render(request, "accounts_login.html", ctx)


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