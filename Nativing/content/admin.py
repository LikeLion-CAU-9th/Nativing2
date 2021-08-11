from django.contrib import admin
from .models import ContentUpload, Tag, SocialSaves, SocialLikes

admin.site.register(ContentUpload)
admin.site.register(Tag)
admin.site.register(SocialSaves)
admin.site.register(SocialLikes)
