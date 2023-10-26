# Generated by Django 4.2.4 on 2023-09-03 04:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_visitor_alter_notice_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='pass_year',
            field=models.PositiveIntegerField(default=2022),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumni',
            name='qualification',
            field=models.TextField(default=12, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateField(default=datetime.date(2023, 9, 3)),
        ),
    ]