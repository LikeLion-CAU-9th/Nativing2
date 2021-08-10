from django.contrib import admin
from .models import ContentUpload, Tag, ContentLikes

admin.site.register(ContentUpload)
admin.site.register(Tag)
admin.site.register(ContentLikes)
