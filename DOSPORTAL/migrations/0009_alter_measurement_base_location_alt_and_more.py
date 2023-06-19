# Generated by Django 4.2.1 on 2023-06-05 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOSPORTAL', '0008_record_log_filename_alter_record_measurement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='base_location_alt',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='base_location_lat',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='base_location_lon',
            field=models.FloatField(default=None, null=True),
        ),
    ]
