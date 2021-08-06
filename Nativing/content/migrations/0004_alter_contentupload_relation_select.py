# Generated by Django 3.2.5 on 2021-08-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_contentupload_agree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentupload',
            name='relation_select',
            field=models.CharField(choices=[('FAMILY', '가족'), ('FRIEND', '친구'), ('SENIOR', '선배'), ('WORK', '직장')], default='FAMILY', max_length=20),
        ),
    ]
