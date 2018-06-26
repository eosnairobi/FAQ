# Generated by Django 2.0.6 on 2018-06-26 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0017_mention'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mention',
            name='subject',
        ),
        migrations.AddField(
            model_name='mention',
            name='subject_url',
            field=models.URLField(blank=True),
        ),
    ]
