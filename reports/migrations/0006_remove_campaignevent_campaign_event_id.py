# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-19 00:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20170719_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaignevent',
            name='campaign_event_id',
        ),
    ]