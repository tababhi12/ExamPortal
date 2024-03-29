# Generated by Django 2.1.7 on 2019-06-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userprofile', '0007_auto_20190605_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='level_hr',
            field=models.BooleanField(choices=[('referral', 'Referral'), ('jop_portal', 'Job Portal')], default=False, verbose_name='HR Level Done'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='level_l1',
            field=models.BooleanField(choices=[('referral', 'Referral'), ('jop_portal', 'Job Portal')], default=False, verbose_name='L1 Level Done'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='level_l2',
            field=models.BooleanField(choices=[('referral', 'Referral'), ('jop_portal', 'Job Portal')], default=False, verbose_name='L2 Level Done'),
        ),
    ]
