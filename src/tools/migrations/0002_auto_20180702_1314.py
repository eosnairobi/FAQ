# Generated by Django 2.0.6 on 2018-07-02 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dapp',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='tool',
            name='about',
            field=models.TextField(blank=True),
        ),
    ]
