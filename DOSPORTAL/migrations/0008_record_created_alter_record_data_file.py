# Generated by Django 4.2.11 on 2024-04-04 12:59

import DOSPORTAL.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DOSPORTAL', '0007_record_data_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Time of creation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record',
            name='data_file',
            field=models.FileField(blank=True, help_text='Processed spectral file', null=True, upload_to=DOSPORTAL.models.Record.user_directory_path_data, verbose_name='Log file'),
        ),
    ]
