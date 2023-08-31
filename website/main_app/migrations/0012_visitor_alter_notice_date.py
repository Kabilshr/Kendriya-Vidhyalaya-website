# Generated by Django 4.2.4 on 2023-08-30 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_video_gallery_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.BigIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateField(default=datetime.date(2023, 8, 30)),
        ),
    ]