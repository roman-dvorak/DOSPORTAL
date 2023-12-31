# Generated by Django 4.2.1 on 2023-06-05 08:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('DOSPORTAL', '0002_detectormanufacturer_name_detectormanufacturer_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detector',
            name='manufacturer',
        ),
        migrations.CreateModel(
            name='DetectorType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=80)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DOSPORTAL.detectormanufacturer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='detector',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='DOSPORTAL.detectortype'),
            preserve_default=False,
        ),
    ]
