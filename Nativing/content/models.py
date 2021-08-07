from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from taggit.models import TagBase, TaggedItemBase

from accounts.models import User

EXPRESSION_CHOICES = (
   ('ABBREVIATION','줄임말'),
   ('NEOLOGISM','신조어'),
)

RELATION_CHOICES = (
    ('FAMILY','가족'),   
    ('FRIEND','친구'),
    ('SENIOR', '선배'),
    ('WORK', '직장')
)

class Tag(TagBase):
    unique = True,
    max_length = 100,
    allow_unicode = True,
    en_name = models.CharField(max_length=40, blank=True, null=True)

# Tag 중개모델
class TaggedContent(TaggedItemBase):
    content_object = models.ForeignKey('ContentUpload', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,
        related_name="tagged_content",
    )

class ContentUpload(models.Model):
    title = models.CharField(max_length = 40, )
    expression = models.TextField()
    expression_descript = models.TextField()
    datetime = models.DateTimeField(default = timezone.now)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    tag = TaggableManager(through=TaggedContent)
    agree = models.BooleanField(default=False)

    #핵심표현 설명 선택지
    expression_descript_select = models.CharField(max_length=20, choices=EXPRESSION_CHOICES, default='ABBREVIATION')
    #상대와의 관계 선택지
    relation_select = models.CharField(max_length=20, choices=RELATION_CHOICES, default='FAMILY')

    def __str__(self):
        return self.title



