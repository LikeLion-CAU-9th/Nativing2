# Generated by Django 3.2.5 on 2021-07-30 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentupload',
            name='expression',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contentupload',
            name='expression_descript',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contentupload',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]