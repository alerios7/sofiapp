# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 20:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sofiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='architecture',
            field=models.CharField(blank=True, max_length=200, verbose_name='Arquitectura'),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2016, 11, 10, 20, 14, 13, 890853, tzinfo=utc), verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='project',
            name='landscaping',
            field=models.CharField(blank=True, max_length=200, verbose_name='Paisajismo'),
        ),
    ]
