# Generated by Django 5.0.7 on 2024-08-13 10:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walletmanagement', '0007_recoveryphrase'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_id', models.CharField(max_length=8, unique=True)),
                ('recovery_phrase', models.TextField()),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='RecoveryPhrase',
        ),
        migrations.DeleteModel(
            name='UserPassword',
        ),
    ]