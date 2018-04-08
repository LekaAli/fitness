# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-21 02:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0007_auto_20170721_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 7, 21, 2, 53, 2, 988070, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='serviceprovider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serviceProvider.Serviceprovider'),
        ),
    ]
