# Generated by Django 4.0.6 on 2024-06-14 03:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_dogs_vacunacion_user_available_days_user_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserves_Daily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog', models.ForeignKey(max_length=250, on_delete=django.db.models.deletion.CASCADE, to='main.dogs')),
                ('propietario', models.ForeignKey(max_length=250, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
