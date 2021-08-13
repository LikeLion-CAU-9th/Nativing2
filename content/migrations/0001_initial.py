# Generated by Django 3.2.5 on 2021-08-11 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=12)),
                ('expression', models.CharField(max_length=16)),
                ('expression_descript', models.TextField()),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('agree', models.BooleanField(default=False)),
                ('expression_descript_select', models.CharField(choices=[('ABBREVIATION', '줄임말'), ('NEOLOGISM', '신조어')], default='ABBREVIATION', max_length=20)),
                ('relation_select', models.CharField(choices=[('FAMILY', '가족'), ('FRIEND', '친구'), ('SENIOR', '선배'), ('WORK', '직장')], default='FAMILY', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('en_name', models.CharField(blank=True, max_length=6, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.contentupload')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_content', to='content.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialSaves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_time', models.DateTimeField(auto_now_add=True)),
                ('save_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='save_content', to='content.contentupload', verbose_name='자징 누른 글')),
                ('save_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='save_user', to=settings.AUTH_USER_MODEL, verbose_name='저장 누른 사람')),
            ],
            options={
                'unique_together': {('save_user', 'save_content')},
            },
        ),
        migrations.CreateModel(
            name='SocialLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_time', models.DateTimeField(auto_now_add=True)),
                ('like_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_content', to='content.contentupload', verbose_name='좋아요 누른 글')),
                ('like_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='like_user', to=settings.AUTH_USER_MODEL, verbose_name='좋아요 누른 사람')),
            ],
            options={
                'unique_together': {('like_user', 'like_content')},
            },
        ),
        migrations.AddField(
            model_name='contentupload',
            name='likes',
            field=models.ManyToManyField(related_name='save', through='content.SocialLikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contentupload',
            name='saves',
            field=models.ManyToManyField(related_name='like', through='content.SocialSaves', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contentupload',
            name='tag',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='content.TaggedContent', to='content.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='contentupload',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
    ]
