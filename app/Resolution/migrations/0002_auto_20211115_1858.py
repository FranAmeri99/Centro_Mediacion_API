# Generated by Django 3.2.6 on 2021-11-15 18:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Resolution', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resolutionportfolio',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 11, 15, 18, 58, 58, 421163, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='resolutionsession',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 11, 15, 18, 58, 58, 421623, tzinfo=utc)),
        ),
    ]