# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-21 01:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0013_auto_20170708_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='identitynumber',
            field=models.CharField(default='0000000000000', max_length=13, verbose_name="Patient's Identity Number"),
        ),
        migrations.AlterField(
            model_name='patient',
            name='creationdate',
            field=models.DateField(default=datetime.datetime(2017, 7, 21, 1, 57, 0, 852340, tzinfo=utc), verbose_name="Patient's record creation date"),
        ),
    ]