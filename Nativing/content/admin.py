from django.contrib import admin
from .models import Comment, ContentUpload, Tag, SocialSaves, SocialLikes, ViewHistory 

admin.site.register(ContentUpload)
admin.site.register(Tag)
admin.site.register(SocialSaves)
admin.site.register(SocialLikes)
admin.site.register(ViewHistory)
admin.site.register(Comment)