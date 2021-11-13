# Generated by Django 3.2.8 on 2021-11-13 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0015_delete_frontendsetting'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('mode', models.CharField(choices=[('sandbox', 'Sandbox'), ('production', 'Production')], default='sandbox', max_length=50)),
                ('sandbox_client_id', models.CharField(max_length=255)),
                ('sandbox_secret_key', models.CharField(max_length=255)),
                ('production_client_id', models.CharField(max_length=255)),
                ('production_secret_key', models.CharField(max_length=255)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payment_currency', to='utilities.currency')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
