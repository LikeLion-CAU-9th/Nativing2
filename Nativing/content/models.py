from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

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

class ContentUpload(models.Model):
    title = models.CharField(max_length = 40, )
    expression = models.TextField()
    expression_descript = models.TextField()
    datetime = models.DateTimeField(default = timezone.now)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    tag = TaggableManager()
    #핵심표현 설명 선택지
    expression_descript_select = models.CharField(max_length=20, choices=EXPRESSION_CHOICES, default='ABBREVIATION')
    #상대와의 관계 선택지
    relation_select = models.CharField(max_length=20, choices=RELATION_CHOICES, default='FAMILY')

    def __str__(self):
        return self.title