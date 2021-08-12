from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
     path('upload/', CreateContentUploadView, name='content_upload'),
     # path('explore_test/', explore_test, name = "explore_test"),
     path('explore/', explore, name = "explore"),
     path('explore-filter/', explore_filter, name = "explore_filter"),
     path('explore/<int:content_id>', content_detail, name = "content_detail"),
     path('detail-comment', detail_comment, name = "detaio_comment"),
]