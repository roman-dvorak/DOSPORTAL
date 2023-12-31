# Generated by Django 4.2.2 on 2023-06-24 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DOSPORTAL', '0024_rename_compaings_measurement_campaings'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetectorLogblock',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(verbose_name='Description zásahu')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('detector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DOSPORTAL.detector')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
