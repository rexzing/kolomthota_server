# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-02 04:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_shippingagent_shipping_line'),
        ('shipping_line', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VesselDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vessel_name', models.CharField(max_length=200)),
                ('eta', models.DateTimeField()),
                ('etb', models.DateTimeField()),
                ('dis', models.IntegerField(default=0)),
                ('load', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('loa_val', models.IntegerField()),
                ('vessel_status', models.CharField(choices=[('M', 'Main Line'), ('F', 'Feeder Line')], max_length=2)),
                ('ref_no', models.CharField(max_length=100, unique=True)),
                ('draft_arrival', models.DecimalField(decimal_places=2, max_digits=4)),
                ('draft_departure', models.DecimalField(decimal_places=2, max_digits=4)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('etc', models.DateTimeField()),
                ('modified_time', models.DateTimeField(auto_now_add=True)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('first_confirm', models.BooleanField(default=False)),
                ('second_confirm', models.BooleanField(default=False)),
                ('third_confirm', models.BooleanField(default=False)),
                ('is_at_berth', models.BooleanField(default=False)),
                ('shipping_agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.ShippingAgent')),
            ],
            options={
                'ordering': ['eta'],
            },
        ),
    ]
