# Generated by Django 4.2.3 on 2023-07-21 09:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0003_notice_date_alter_member_list_designation_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notice",
            name="date",
            field=models.DateField(default=datetime.date(2023, 7, 21)),
        ),
    ]
