# Generated by Django 3.1.3 on 2022-03-23 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20220323_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classattendance',
            name='close_time',
            field=models.TimeField(default=datetime.time),
        ),
        migrations.AlterField(
            model_name='classattendance',
            name='create_time',
            field=models.TimeField(default=datetime.time),
        ),
    ]