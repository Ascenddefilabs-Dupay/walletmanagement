# Generated by Django 5.0.7 on 2024-08-05 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('walletmanagement', '0003_rename_password_walletpassword_wallet_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WalletPassword',
            new_name='UserPassword',
        ),
        migrations.RenameField(
            model_name='userpassword',
            old_name='wallet_password',
            new_name='password',
        ),
    ]