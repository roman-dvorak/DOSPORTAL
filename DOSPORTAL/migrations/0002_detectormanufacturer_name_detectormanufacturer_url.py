# Generated by Django 4.2.1 on 2023-06-05 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOSPORTAL', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detectormanufacturer',
            name='name',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detectormanufacturer',
            name='url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]