# Generated by Django 5.1.3 on 2025-02-01 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='available_days',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='rewards',
            field=models.IntegerField(default=0),
        ),
    ]
