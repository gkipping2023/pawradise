# Generated by Django 5.1.3 on 2025-01-22 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_reserves_daily_propietario'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserves_daily',
            name='is_checked_in',
            field=models.BooleanField(default=False),
        ),
    ]