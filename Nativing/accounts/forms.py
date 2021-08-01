from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "nickname", "date_of_birth", "user_image", "user_gender"]


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]
        widgets = {"password": forms.PasswordInput}