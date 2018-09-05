# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-02 03:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_line', '0001_initial'),
        ('accounts', '0003_shippingagent_is_active_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingagent',
            name='shipping_line',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='shipping_line.ShippingLine'),
        ),
    ]
