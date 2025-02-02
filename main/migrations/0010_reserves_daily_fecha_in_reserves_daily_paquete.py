# Generated by Django 4.0.6 on 2024-06-14 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_reserves_daily_propietario'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserves_daily',
            name='fecha_in',
            field=models.DateField(default='1900-01-01'),
        ),
        migrations.AddField(
            model_name='reserves_daily',
            name='paquete',
            field=models.CharField(choices=[('medio', 'Medio dia - $7.49'), ('1dia', 'Pase Diario - $12.84'), ('3dia', 'Pase 3 dias - $35.31'), ('6dia', 'Pase 6 dias - $64.20'), ('12dia', 'Pase 12 dias - $117.70'), ('24dia', 'Pase 24 dias - $214.00')], default='None', max_length=250),
        ),
    ]
