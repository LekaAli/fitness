# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-02 15:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0010_auto_20170702_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='creationdate',
            field=models.DateField(default=datetime.datetime(2017, 7, 2, 15, 30, 41, 92637, tzinfo=utc)),
        ),
    ]
