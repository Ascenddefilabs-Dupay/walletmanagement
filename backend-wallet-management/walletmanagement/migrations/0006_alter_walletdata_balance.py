# Generated by Django 4.2.16 on 2024-09-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walletmanagement', '0005_walletdata_balance_walletdata_sui_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletdata',
            name='balance',
            field=models.CharField(default='null', max_length=20),
        ),
    ]
