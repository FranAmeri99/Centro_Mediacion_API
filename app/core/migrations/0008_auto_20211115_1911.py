# Generated by Django 3.2.6 on 2021-11-15 19:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20211115_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediationportafolio',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 11, 15, 19, 11, 54, 822334, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mediationportafolio',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 11, 15, 19, 11, 54, 822310, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mediationsessions',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 11, 15, 19, 11, 54, 822842, tzinfo=utc)),
        ),
    ]
