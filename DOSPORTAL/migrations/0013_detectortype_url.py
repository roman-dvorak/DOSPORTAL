# Generated by Django 4.2.11 on 2024-04-04 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOSPORTAL', '0012_alter_detectortype_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='detectortype',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]