# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-08 10:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0012_auto_20170702_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='status',
            field=models.IntegerField(choices=[(0, 'created'), (1, 'updated'), (2, 'deleted')], default='0', verbose_name='Patient account status'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='creationdate',
            field=models.DateField(default=datetime.datetime(2017, 7, 8, 10, 3, 9, 861136, tzinfo=utc), verbose_name="Patient's record creation date"),
        ),
    ]
