# Generated by Django 4.2.2 on 2023-06-24 22:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DOSPORTAL', '0025_detectorlogblock'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetectorLogbook',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(verbose_name='Description zásahu')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('detector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logbook', to='DOSPORTAL.detector')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='DetectorLogblock',
        ),
    ]
