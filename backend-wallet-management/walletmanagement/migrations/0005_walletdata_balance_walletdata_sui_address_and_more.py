# Generated by Django 4.2.16 on 2024-09-23 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walletmanagement', '0004_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='walletdata',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='walletdata',
            name='sui_address',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='walletdata',
            name='password',
            field=models.CharField(default='null', max_length=128),
        ),
        migrations.AlterField(
            model_name='walletdata',
            name='recovery_phrases',
            field=models.TextField(default='null'),
        ),
    ]
