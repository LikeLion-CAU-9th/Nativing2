from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('detail-save/', social_save, name = "content_save"),
    path('social-follow/', social_follow, name = "social_follow"),
    path('social-likes', social_likes, name = "social_likes"),
]
