# Generated by Django 4.2.16 on 2024-09-20 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZkLogin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_id', models.CharField(blank=True, max_length=10, unique=True)),
                ('sui_address', models.CharField(max_length=255)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.DeleteModel(
            name='ZkLogin',
        ),
    ]
