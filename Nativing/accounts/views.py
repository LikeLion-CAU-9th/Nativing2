from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def accounts_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            if request.POST.get("date_of_birth"):
                date_str = request.POST.get("date_of_birth")
                date_of_birth = datetime.strptime(date_str, "%Y-%m-%d").date()
                time_now = datetime.now().date()
                days_lived = (time_now - date_of_birth).days
                instance.user_age = days_lived // 365
            else: 
                instance.user_age = 20

            instance.save()
            form.save_m2m()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email = email, password = raw_password)
            login(request, user)
            
            return redirect("main")
            #TODO 추후 회원가입 후 개인 프로필로 redirect 되도록 설정 필요
        else:
            print(form.errors)
            ctx = {
                "form": form,
                "error": form.errors
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
        print(user)
        print(form.errors)
        if user is not None:
            auth_login(request, user)
            return redirect("main")
        else:
            ctx = {
                "form": form,
                "error": "Email and password do not match",
            }
            return render(request, "accounts_login.html", ctx)
    elif request.method == "GET":
        form = LoginForm()
        ctx = {
            "form": form,
        }
        return render(request, "accounts_login.html", ctx)


def accounts_logout(request):
    auth_logout(request)
    return redirect("main")


def accounts_home(request):
    return render(request, "accounts_home.html")


def signup_success(request):
    return render(request, "signup_success.html")


def login_success(request):
    return render(request, "login_success.html")


def logout_success(request):
    return render(request, "logout_success.html")