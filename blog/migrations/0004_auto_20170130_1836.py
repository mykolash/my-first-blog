# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 16:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170130_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 30, 16, 36, 45, 775208, tzinfo=utc)),
        ),
    ]
