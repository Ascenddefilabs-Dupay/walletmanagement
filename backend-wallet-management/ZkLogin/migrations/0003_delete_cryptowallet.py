# Generated by Django 4.2.16 on 2024-09-23 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ZkLogin', '0002_cryptowallet_delete_zklogin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CryptoWallet',
        ),
    ]
