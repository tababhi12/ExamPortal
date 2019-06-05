# Generated by Django 2.1.7 on 2019-06-05 21:42

import Userprofile.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userprofile', '0013_auto_20190606_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='level_hr',
            field=models.CharField(choices=[('true', 'True'), ('false', 'False')], max_length=120, validators=[Userprofile.validators.validate_level_hr], verbose_name='HR Level Done'),
        ),
    ]
