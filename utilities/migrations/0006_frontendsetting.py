# Generated by Django 3.2.8 on 2021-11-02 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0005_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontendSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='frontends/')),
            ],
        ),
    ]
