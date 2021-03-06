# Generated by Django 3.2.9 on 2021-11-15 21:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20211115_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediationportafolio',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 11, 15, 21, 38, 40, 46385, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mediationportafolio',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 11, 15, 21, 38, 40, 46355, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mediationsessions',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 11, 15, 21, 38, 40, 46779, tzinfo=utc)),
        ),
    ]
