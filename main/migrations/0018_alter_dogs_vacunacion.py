# Generated by Django 5.1.3 on 2025-02-06 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_user_available_days_alter_user_rewards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogs',
            name='vacunacion',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/vacunacion'),
        ),
    ]
