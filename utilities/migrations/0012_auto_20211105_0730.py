# Generated by Django 3.2.8 on 2021-11-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0011_auto_20211105_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='banner',
            field=models.ImageField(help_text='Upload banner image(2000x1335)px', null=True, upload_to='banner/'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='dark_logo',
            field=models.ImageField(help_text='Upload dark logo(330x70)px', null=True, upload_to='logos/'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='favicon',
            field=models.ImageField(help_text='Upload dark logo(90x90)px', null=True, upload_to='logos/'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='light_logo',
            field=models.ImageField(help_text='Upload light logo(330x70)px', null=True, upload_to='logos/'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='small_logo',
            field=models.ImageField(help_text='Upload dark logo(49x58)px', null=True, upload_to='logos/'),
        ),
    ]