# Generated by Django 3.2.6 on 2021-11-15 19:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Resolution', '0005_auto_20211115_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resolutionportfolio',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 11, 15, 19, 11, 54, 823281, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='resolutionsession',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 11, 15, 19, 11, 54, 823657, tzinfo=utc)),
        ),
    ]