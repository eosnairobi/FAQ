# Generated by Django 2.0.6 on 2018-06-26 20:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0018_auto_20180626_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='mention',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]