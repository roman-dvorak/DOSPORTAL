# Generated by Django 4.2.2 on 2023-06-24 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOSPORTAL', '0021_measurement_campaign_alter_detector_calib_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement_campaign',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='measurement name'),
        ),
    ]
