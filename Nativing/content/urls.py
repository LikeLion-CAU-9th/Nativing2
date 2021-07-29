from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', content, name = "content"),
    path('detail', contentDetail, name = "detail"),
    path('explore', explore, name = "explore"),
    path('learning', learningCenter, name = "learning"),
    
]