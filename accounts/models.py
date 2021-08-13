from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from datetime import date, datetime, timedelta


class CustomAccountManager(BaseUserManager):
    def create_user(
        self,
        name, 
        email, 
        nickname,
        date_of_birth,
        user_image,
        user_gender,
        password=None
    ):
        user = self.model(
            name=name,
            email=email, 
            nickname=nickname, 
            date_of_birth=date_of_birth,
            user_image=user_image,
            user_gender=user_gender,
        )
        
        user.set_password(password)
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        name, 
        email, 
        nickname, 
        password
    ):
        user = self.model(
            email=email, 
            name=name,
            nickname=nickname, 
            password=password)
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


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


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(max_length=15, blank=True, null=True, unique=True)
    joined_on = models.DateTimeField(auto_now_add=True)
    withdrew_at = models.DateTimeField(blank=True, null=True)
    date_of_birth =models.DateField(null=True)
    user_image = models.ImageField(upload_to='user_image/', blank=True, null=True, default = "user_image/user_default.jpg")
    user_gender = models.CharField(max_length=10, choices=Gender.GENDER_TYPES)
    user_age = models.PositiveIntegerField(blank=True, null=True, default= 20)
    is_login = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'nickname']

    def __str__(self):
        return self.email
        
    @property
    def is_staff(self):
        return self.is_admin

class Follow(models.Model):
    follower = models.ForeignKey("User", verbose_name="팔로잉 하는 사람", related_name = "follower", on_delete=models.CASCADE, null=True)
    followee = models.ForeignKey("User", verbose_name="팔로잉 당하는 사람", related_name="followee", on_delete=models.CASCADE, null=True)
    follow_time = models.DateTimeField(auto_now_add=True)
