# Generated by Django 5.0.7 on 2024-08-13 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('walletmanagement', '0011_rename_recovery_phrases_walletdata_phrases'),
    ]

    operations = [
        migrations.RenameField(
            model_name='walletdata',
            old_name='phrases',
            new_name='recoveryWords',
        ),
    ]