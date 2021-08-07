from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
     path('upload/', views.CreateContentUploadView.as_view(), name='content_upload'),
     path('explore/', explore, name = "explore"),
     path('explore2/', explore2, name = "explore2"),
     path('explore-filter/', explore_filter, name = "explore_filter"),
     path('tags-to-json/', tags_to_json, name = "tags_to_json"),
     path('explore/<int:content_id>', content_detail, name = "content_detail"),
]