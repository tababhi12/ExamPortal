# Generated by Django 2.1.7 on 2019-05-31 23:11

import Userprofile.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userprofile', '0003_auto_20190601_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='status_l1',
            field=models.CharField(choices=[('pending', 'Pending'), ('hired', 'Hired'), ('reject', 'Reject')], default='pending', max_length=10, validators=[Userprofile.validators.validate_status_l1], verbose_name='L1 Status'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='status_l2',
            field=models.CharField(choices=[('pending', 'Pending'), ('hired', 'Hired'), ('reject', 'Reject')], default='pending', max_length=10, validators=[Userprofile.validators.validate_status_l1], verbose_name='L2 Status'),
        ),
    ]
