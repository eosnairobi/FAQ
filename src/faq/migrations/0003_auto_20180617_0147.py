# Generated by Django 2.0.6 on 2018-06-16 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_question_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
