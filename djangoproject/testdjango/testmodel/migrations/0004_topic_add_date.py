# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 03:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testmodel', '0003_auto_20170802_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 8, 2, 3, 47, 4, 736697, tzinfo=utc)),
            preserve_default=False,
        ),
    ]