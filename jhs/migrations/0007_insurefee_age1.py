# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jhs', '0006_insurefee'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurefee',
            name='age1',
            field=models.FloatField(blank=True, default=0, max_length=10),
        ),
    ]
