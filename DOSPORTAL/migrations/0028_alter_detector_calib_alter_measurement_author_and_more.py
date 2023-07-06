# Generated by Django 4.2.3 on 2023-07-04 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DOSPORTAL', '0027_alter_measurement_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detector',
            name='calib',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detectors', to='DOSPORTAL.detectorcalib'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='campaings',
            field=models.ManyToManyField(blank=True, related_name='Campaigns', to='DOSPORTAL.measurement_campaign'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='description',
            field=martor.models.MartorField(blank=True, verbose_name='Measurement description'),
        ),
        migrations.AlterField(
            model_name='record',
            name='detector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='records', to='DOSPORTAL.detector'),
        ),
    ]
