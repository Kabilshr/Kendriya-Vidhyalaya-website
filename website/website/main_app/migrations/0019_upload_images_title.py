# Generated by Django 4.2 on 2023-06-06 10:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_upload_images_remove_news_and_events_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_images',
            name='title',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
