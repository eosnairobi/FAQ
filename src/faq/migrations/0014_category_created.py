# Generated by Django 2.0.6 on 2018-06-24 22:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0013_category_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]