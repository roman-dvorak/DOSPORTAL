# Generated by Django 4.2.2 on 2023-06-22 14:54

import DOSPORTAL.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DOSPORTAL', '0015_alter_measurement_flight'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='record_type',
            field=models.CharField(choices=[('S', 'Spectral measurements'), ('L', 'Location (GPX, FR24, NMEA)')], default='S', help_text='Type of log file', verbose_name='Certain record type, enum'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='base_location_alt',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='base_location_lat',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='base_location_lon',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='location_file',
            field=models.FileField(blank=True, upload_to=DOSPORTAL.models.measurement.user_directory_path, verbose_name='File log'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='measurement_type',
            field=models.CharField(choices=[('D', 'Debug measurement'), ('S', 'Static measurement'), ('M', 'Mobile measurement (ground)'), ('C', 'Civil airborne measurement'), ('A', 'Special airborne measurement')], default='S', help_text='Type of measurement', verbose_name='Certain measurement type, enum'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='time_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Measurement beginning time'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='time_start',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Measurement beginning time'),
        ),
        migrations.AlterField(
            model_name='record',
            name='detector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DOSPORTAL.detector'),
        ),
    ]
