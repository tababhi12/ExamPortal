# Generated by Django 2.1.7 on 2019-05-28 06:24

import Employeeprofile.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employeeprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=120, unique=True, validators=[Employeeprofile.validators.validate_userid], verbose_name='Username')),
                ('first_name', models.CharField(max_length=120, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=120, verbose_name='Last Name')),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=120, verbose_name='Gender')),
                ('empid', models.IntegerField(unique=True, verbose_name='Employee ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, validators=[Employeeprofile.validators.validate_email], verbose_name='Email')),
                ('phone', models.BigIntegerField(blank=True, null=True, unique=True, validators=[Employeeprofile.validators.validate_phone], verbose_name='Phone Number')),
                ('skill', models.SlugField(choices=[('python', 'Python'), ('java', 'Java')], default='python', verbose_name='Skill')),
                ('level', models.CharField(choices=[('l1', 'L1'), ('l2', 'L2')], max_length=120)),
                ('hired', models.IntegerField(blank=True, default=0, null=True, verbose_name='Total hired')),
                ('rejected', models.IntegerField(blank=True, default=0, null=True, verbose_name='Total rejected')),
                ('security_token', models.CharField(max_length=200, validators=[Employeeprofile.validators.validate_security_token], verbose_name='Secure_token')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
            ],
            options={
                'verbose_name': 'interviewer',
                'verbose_name_plural': 'interviewers',
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
    ]
