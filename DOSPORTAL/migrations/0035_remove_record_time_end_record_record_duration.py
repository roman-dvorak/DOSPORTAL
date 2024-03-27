# Generated by Django 4.2.7 on 2023-12-03 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOSPORTAL', '0034_record_metadata_alter_detector_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='time_end',
        ),
        migrations.AddField(
            model_name='record',
            name='record_duration',
            field=models.DurationField(help_text='Duration of record', null=True, verbose_name='Record duration'),
        ),
    ]