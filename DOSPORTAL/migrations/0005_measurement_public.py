# Generated by Django 4.2.1 on 2023-06-05 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOSPORTAL', '0004_alter_measurement_measurement_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='public',
            field=models.BooleanField(default=True, verbose_name='Will be data publicly available'),
        ),
    ]
