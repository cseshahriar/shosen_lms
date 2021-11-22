# Generated by Django 3.2.8 on 2021-11-14 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0003_auto_20211029_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='facebook_profile_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='linkedin_profile_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter_profile_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='biography',
            field=models.TextField(blank=True, help_text='A short description about yourself', null=True),
        ),
    ]