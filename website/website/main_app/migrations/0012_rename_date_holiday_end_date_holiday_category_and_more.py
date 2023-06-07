# Generated by Django 4.2 on 2023-06-05 11:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_remove_holiday_file_remove_holiday_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='holiday',
            old_name='date',
            new_name='end_date',
        ),
        migrations.AddField(
            model_name='holiday',
            name='category',
            field=models.CharField(choices=[('holiday', 'Holiday'), ('summer_vacation', 'Summer Vacation'), ('winter_vacation', 'Winter Vacation'), ('autum_vacation', 'Autum Vacation')], default=django.utils.timezone.now, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='holiday',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]