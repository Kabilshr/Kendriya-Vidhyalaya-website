# Generated by Django 4.2 on 2023-06-29 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0034_class1_class11'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='gallery',
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
    ]
