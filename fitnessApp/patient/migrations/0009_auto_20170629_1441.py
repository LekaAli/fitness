# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-29 12:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_auto_20170629_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='creationdate',
            field=models.DateField(default=datetime.datetime(2017, 6, 29, 12, 41, 59, 231570, tzinfo=utc)),
        ),
    ]