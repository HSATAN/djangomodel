# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmodel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
