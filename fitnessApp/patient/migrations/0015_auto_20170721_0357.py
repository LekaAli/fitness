# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-21 01:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0014_auto_20170721_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='creationdate',
            field=models.DateField(default=datetime.datetime(2017, 7, 21, 1, 57, 8, 884269, tzinfo=utc), verbose_name="Patient's record creation date"),
        ),
        migrations.AlterField(
            model_name='patient',
            name='identitynumber',
            field=models.CharField(max_length=13, verbose_name="Patient's Identity Number"),
        ),
    ]
