# Generated by Django 4.2.11 on 2024-03-28 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOSPORTAL', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='metadata',
            new_name='metadatar',
        ),
    ]