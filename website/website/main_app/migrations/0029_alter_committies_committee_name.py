# Generated by Django 4.2 on 2023-06-08 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0028_remove_committies_members_committies_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committies',
            name='Committee_name',
            field=models.TextField(choices=[('Admissions', 'Admissions'), ('Academic advisory', 'Academic_Advisory'), ('Examination', 'Examination'), ('Transpotation', 'Transpotation')]),
        ),
    ]