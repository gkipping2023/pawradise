# Generated by Django 4.0.6 on 2024-06-14 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_reserves_daily'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserves_daily',
            name='propietario',
            field=models.OneToOneField(max_length=250, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
