# Generated by Django 3.0 on 2020-07-07 19:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0016_booking_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='expiresDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 7, 19, 11, 9, 681478, tzinfo=utc)),
        ),
    ]
