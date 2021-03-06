# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-07 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_line', '0004_auto_20180905_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vessel_name', models.CharField(max_length=200)),
                ('loa_val', models.DecimalField(decimal_places=2, max_digits=6)),
                ('vessel_status', models.CharField(choices=[('M', 'Main Line'), ('F', 'Feeder Line')], max_length=2)),
            ],
            options={
                'verbose_name': 'Vessel',
                'verbose_name_plural': 'Vessels',
            },
        ),
        migrations.RemoveField(
            model_name='vesseldetails',
            name='loa_val',
        ),
        migrations.RemoveField(
            model_name='vesseldetails',
            name='vessel_name',
        ),
        migrations.RemoveField(
            model_name='vesseldetails',
            name='vessel_status',
        ),
        migrations.AddField(
            model_name='vesseldetails',
            name='vessel',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='shipping_line.Vessel'),
            preserve_default=False,
        ),
    ]
