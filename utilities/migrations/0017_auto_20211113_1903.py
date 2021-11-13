# Generated by Django 3.2.8 on 2021-11-13 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0016_paymentsettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMTPSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protocaol', models.CharField(choices=[('smtp', 'SMTP'), ('pop3', 'POP3'), ('imap', 'IMAP')], default='smtp', max_length=50)),
                ('host', models.URLField(max_length=255)),
                ('port', models.PositiveIntegerField()),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'SMTP Setting',
                'verbose_name_plural': 'SMTP Settings',
            },
        ),
        migrations.AlterModelOptions(
            name='paymentsettings',
            options={'verbose_name': 'Payment Setting', 'verbose_name_plural': 'Payment Settings'},
        ),
    ]