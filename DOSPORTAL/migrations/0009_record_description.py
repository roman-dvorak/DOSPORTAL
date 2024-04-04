# Generated by Django 4.2.11 on 2024-04-04 16:43

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('DOSPORTAL', '0008_record_created_alter_record_data_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='description',
            field=markdownx.models.MarkdownxField(blank=True, help_text='Description of the record', verbose_name='Description'),
        ),
    ]
