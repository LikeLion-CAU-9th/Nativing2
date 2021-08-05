from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('content/', include('content.urls')),
    path('upload/', include('upload.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)