# Generated by Django 4.2.11 on 2024-04-05 02:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOSPORTAL', '0013_detectortype_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detector',
            name='data',
            field=models.JSONField(blank=True, default=[{}], help_text='Detector metadata, used for advanced data processing and maintaining', verbose_name='Detector metadata'),
        ),
        migrations.AlterField(
            model_name='record',
            name='metadata',
            field=models.JSONField(blank=True, default='[{}]', help_text='record metadata, used for advanced data processing and maintaining', verbose_name='record_metadata'),
        ),
        migrations.AlterField(
            model_name='record',
            name='time_start',
            field=models.DateTimeField(default=datetime.datetime(2000, 1, 1, 0, 0), null=True, verbose_name='Measurement beginning time'),
        ),
    ]
