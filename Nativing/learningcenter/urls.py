from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', learning_center, name = "learning"),
    path('saved-contents/', saved_contents, name = "saved_contents"),
    path('view-history/', view_history, name = "view_history"),
]