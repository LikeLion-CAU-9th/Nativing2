from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
     path('upload/', views.CreateContentUploadView.as_view(), name='content_upload'),
     path('explore/', explore, name = "explore"),
     path('explore-filter/', explore_filter, name = "explore_filter")
]