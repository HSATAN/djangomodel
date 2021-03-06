# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 03:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testmodel', '0002_test_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='test',
            name='age',
        ),
        migrations.AddField(
            model_name='article',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testmodel.Topic'),
        ),
    ]
