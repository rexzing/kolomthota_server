# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-01-30 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_line', '0015_vessel_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='vesselarrival',
            name='is_rejected_BP',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vesselarrival',
            name='is_rejected_user',
            field=models.BooleanField(default=False),
        ),
    ]
