# Generated by Django 4.2.3 on 2023-07-05 21:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('DOSPORTAL', '0028_alter_detector_calib_alter_measurement_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CARImodel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('data', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='flight',
            name='cari',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DOSPORTAL.carimodel'),
        ),
    ]