# Generated by Django 4.2.2 on 2023-06-23 23:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DOSPORTAL', '0017_airports_municipality_airports_web_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetectorCalib',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(verbose_name='Calibration name')),
                ('description', models.TextField(verbose_name='Description of calibration status')),
                ('date', models.DateTimeField()),
                ('cabib', models.CharField(verbose_name='Slozky kalibrace, json')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]