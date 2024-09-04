# Generated by Django 5.0.7 on 2024-09-04 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WalletData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_id', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('recovery_phrases', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.CharField(default='null', max_length=10)),
            ],
            options={
                'db_table': 'crypto_wallet_table',
            },
        ),
    ]
