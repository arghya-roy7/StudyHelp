# Generated by Django 3.2.22 on 2023-12-08 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20231208_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroutine',
            name='end_time',
            field=models.TimeField(),
        ),
    ]
