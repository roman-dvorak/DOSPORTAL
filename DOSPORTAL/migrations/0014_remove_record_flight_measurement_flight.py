# Generated by Django 4.2.2 on 2023-06-22 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DOSPORTAL', '0013_rename_callsign_flight_flight_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='flight',
        ),
        migrations.AddField(
            model_name='measurement',
            name='flight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='record', to='DOSPORTAL.flight', verbose_name='Reference na objekt s informacemi o letu'),
        ),
    ]