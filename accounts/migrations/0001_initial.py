# Generated by Django 3.2.5 on 2021-08-11 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('nickname', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('joined_on', models.DateTimeField(auto_now_add=True)),
                ('withdrew_at', models.DateTimeField(blank=True, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('user_image', models.ImageField(blank=True, default='user_image/user_default.jpg', null=True, upload_to='user_image/')),
                ('user_gender', models.CharField(choices=[('male', '남성'), ('female', '여성')], max_length=10)),
                ('user_age', models.PositiveIntegerField(blank=True, default=20, null=True)),
                ('is_login', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_time', models.DateTimeField(auto_now_add=True)),
                ('followee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followee', to=settings.AUTH_USER_MODEL, verbose_name='팔로잉 당하는 사람')),
                ('follower', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='팔로잉 하는 사람')),
            ],
        ),
    ]
