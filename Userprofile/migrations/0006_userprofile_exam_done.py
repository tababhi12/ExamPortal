# Generated by Django 2.1.7 on 2019-06-05 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userprofile', '0005_auto_20190605_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='exam_done',
            field=models.BooleanField(default=False, verbose_name='Exam Status'),
        ),
    ]