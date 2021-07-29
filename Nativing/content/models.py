from django.db import models
from django.db.models.fields import related
from django.db.models.fields.related import ForeignKey
from ..upload.models import Content_upload

class ContentComment(models.model):
    content = models.ForeignKey(Content_upload, on_delete=models.CASCADE, related_name="comments")
    # account model 추가되면 추가 
    author = 0
    body = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.body[:10]
