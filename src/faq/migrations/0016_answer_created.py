# Generated by Django 2.0.6 on 2018-06-25 21:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0015_auto_20180625_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
