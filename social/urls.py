from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('social-follow/', social_follow, name = "social_follow"),
]