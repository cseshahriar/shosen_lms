# Generated by Django 3.2.8 on 2021-11-04 19:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0009_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_name', models.CharField(default='Shosen LMS', max_length=255)),
                ('website_title', models.CharField(default='Shosen Learning Management', max_length=255)),
                ('website_meta_key', models.CharField(help_text='Please add comma separated values', max_length=255)),
                ('website_meta_description', models.TextField()),
                ('author', models.CharField(default='Author name', max_length=255)),
                ('slogan', models.CharField(default='Slogan', max_length=255)),
                ('info_email', models.EmailField(default='info@example.com', max_length=254)),
                ('sales_email', models.EmailField(default='sales@example.com', max_length=254)),
                ('support_email', models.EmailField(default='support@example.com', max_length=254)),
                ('address', models.TextField(default='Address')),
                ('phone', models.CharField(blank=True, max_length=14, null=True, validators=[django.core.validators.RegexValidator('^(?:\\+?88)?01[15-9]\\d{8}$', message='Format (ex: 01234567890)')], verbose_name='Mobile Phone')),
                ('youtube_api_key', models.CharField(default='ACbcad883c9c3e9d9913a715557dddff99', max_length=255)),
                ('vimeo_api_key', models.CharField(default='ACbcad883c9c3e9d9913a715557dddff99', max_length=255)),
                ('purchase_code', models.CharField(default='ABC001', max_length=255)),
                ('student_email_verification', models.BooleanField(default=False)),
                ('footer_text', models.TextField(max_length=255, null=True)),
                ('footer_link', models.CharField(max_length=255, null=True)),
                ('twilio_account_sid', models.CharField(default='ACbcad883c9c3e9d9913a715557dddff99', max_length=255)),
                ('twilio_auth_token', models.CharField(default='abd4d45dd57dd79b86dd51df2e2a6cd5', max_length=255)),
                ('twilio_phone_number', models.CharField(default='+15006660005', max_length=255)),
                ('system_language', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='utilities.language')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
