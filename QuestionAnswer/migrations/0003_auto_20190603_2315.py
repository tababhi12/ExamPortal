# Generated by Django 2.1.7 on 2019-06-03 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionAnswer', '0002_auto_20190603_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionanswer',
            name='answer',
            field=models.CharField(choices=[('a', 'Choice A'), ('b', 'Choice B'), ('c', 'Choice C'), ('d', 'Choice D')], default='a', max_length=220, verbose_name='Answer'),
        ),
    ]
