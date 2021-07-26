from django.db import models
from taggit.managers import TaggableManager

EXPRESSION_CHOICES = (
    ('abbreviation','ABBREVIATION'),
)

RELATION_CHOICES = (
    ('family','FAMILY'),
    ('FRIEND', 'friend'),
)

class Content_upload(models.Model):
    #제목, 핵심표현, 핵심표현 설명(선택지 + 줄글), 상대와의 관계(선택지), 태그(아마 선택지?), 이미지

    title = models.CharField(max_length = 40, help_text="제목")
    expression = models.TextField(help_text="핵심 표현")
    expression_descript = models.TextField(help_text="핵심 표현 설명")
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    tag = TaggableManager()

    #핵심표현 설명 선택지
    expression_descript_select = models.CharField(max_length=10, choices=EXPRESSION_CHOICES, default='abbreviation')
    #상대와의 관계 선택지
    relation_select = models.CharField(max_length=10, choices=RELATION_CHOICES, default='family')

    def __str__(self):
        return self.title
