# Generated by Django 4.2.2 on 2023-06-24 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOSPORTAL', '0023_alter_detectorcalib_cabib'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='compaings',
            new_name='campaings',
        ),
    ]
