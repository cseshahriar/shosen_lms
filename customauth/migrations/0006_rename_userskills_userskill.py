# Generated by Django 3.2.8 on 2021-11-14 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0005_userskills'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserSkills',
            new_name='UserSkill',
        ),
    ]