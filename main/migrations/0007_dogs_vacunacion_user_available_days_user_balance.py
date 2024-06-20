# Generated by Django 4.0.6 on 2024-06-13 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_dogs_is_special_dogs_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogs',
            name='vacunacion',
            field=models.ImageField(blank=True, null=True, upload_to='images/vacunacion'),
        ),
        migrations.AddField(
            model_name='user',
            name='available_days',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
            preserve_default=False,
        ),
    ]
