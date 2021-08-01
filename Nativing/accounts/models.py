from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Gender:
    """
    Gender
    - Distinguish Male, Female
    """
    MALE = 'male'
    FEMALE = 'female'

    GENDER_TYPES = [
        (MALE, '남성'),
        (FEMALE, '여성'),
    ]



class User(AbstractBaseUser):
    username = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='email',
    )
    nickname = models.CharField(max_length=15, blank=True, null=True, unique=True)
    joined_on = models.DateTimeField(auto_now_add=True)
    withdrew_at = models.DateTimeField(blank=True, null=True, verbose_name='탈퇴 시점')
    date_of_birth = models.CharField(max_length=32, blank=True, help_text='생년월일')
    user_image = models.ImageField(upload_to='images/', blank=True, null=True)
    user_gender = models.CharField(max_length=10, choices=Gender.GENDER_TYPES)
    user_age = models.PositiveIntegerField(blank=True, null=True)
    is_login = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
