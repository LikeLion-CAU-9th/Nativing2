# Generated by Django 3.2.5 on 2021-08-09 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210810_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(blank=True, default='user_image/user_default.jpeg', null=True, upload_to='user_image/'),
        ),
    ]