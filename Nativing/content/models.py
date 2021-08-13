from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ForeignKey
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone
from numpy import mod
from numpy.core.numeric import ones
from numpy.lib.arraysetops import unique
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
    max_length = 6,
    allow_unicode = True,
    en_name = models.CharField(max_length=6, blank=True, null=True)

# Tag 중개모델
class TaggedContent(TaggedItemBase):
    content_object = models.ForeignKey('ContentUpload', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,
        related_name="tagged_content",
    )

class ContentUpload(models.Model):
    writer = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name="작성자", related_name="content")
    title = models.CharField(max_length = 12, )
    expression = models.CharField(max_length = 16, )
    expression_descript = models.TextField()
    datetime = models.DateTimeField(default = timezone.now)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    tag = TaggableManager(through=TaggedContent)
    agree = models.BooleanField(default=False)
    saves = models.ManyToManyField(User, through="SocialSaves", related_name="likes")
    likes = models.ManyToManyField(User, through="SocialLikes", related_name="saves")

    #핵심표현 설명 선택지
    expression_descript_select = models.CharField(max_length=20, choices=EXPRESSION_CHOICES, default='ABBREVIATION')
    #상대와의 관계 선택지
    relation_select = models.CharField(max_length=20, choices=RELATION_CHOICES, default='FAMILY')

    def __str__(self):
        return self.title

class SocialSaves(models.Model):
    save_user = models.ForeignKey(User, verbose_name="저장 누른 사람", related_name="save_user", on_delete= models.SET_NULL, null = True)
    save_content = models.ForeignKey(ContentUpload, verbose_name="자징 누른 글", related_name= "save_content", on_delete= models.CASCADE) 
    save_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = [['save_user', 'save_content']]

class SocialLikes(models.Model):
    like_user = models.ForeignKey(User, verbose_name="좋아요 누른 사람", related_name= "like_user", on_delete=models.SET_NULL, null=True)
    like_content = models.ForeignKey(ContentUpload, verbose_name= "좋아요 누른 글", related_name="like_content", on_delete=models.CASCADE)
    like_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['like_user', 'like_content']]

class ViewHistory(models.Model):
    view_user = models.ForeignKey(User, verbose_name="조회한 사람", related_name="view_user", on_delete=models.CASCADE)
    view_content = models.ForeignKey(ContentUpload,verbose_name="조회한 글", related_name="view_content", on_delete=models.CASCADE)
    view_time = models.DateTimeField()


class Comment(models.Model):
    comment_writer = models.ForeignKey(User, verbose_name= "댓글 작성자", related_name="comment_writer", on_delete=models.CASCADE)
    comment_content = models.ForeignKey(ContentUpload, verbose_name="댓글 원 글", related_name="comment_content", on_delete=models.CASCADE)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:20]
    