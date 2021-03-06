# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-26 02:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0020_auto_20170722_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={},
        ),
        migrations.AlterField(
            model_name='patient',
            name='creationdate',
            field=models.DateField(default=datetime.datetime(2017, 7, 26, 2, 50, 0, 621179, tzinfo=utc), verbose_name="Patient's record creation date"),
        ),
        migrations.AlterUniqueTogether(
            name='patient',
            unique_together=set([]),
        ),
        migrations.AddField(
            model_name='child',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child', to='patient.Parent'),
        ),
        migrations.AlterUniqueTogether(
            name='child',
            unique_together=set([('child', 'order')]),
        ),
    ]
