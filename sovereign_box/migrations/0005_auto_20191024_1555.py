# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-10-24 15:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sovereign_box', '0004_auto_20191024_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cointaglink',
            old_name='reports',
            new_name='coin_tag',
        ),
        migrations.RenameField(
            model_name='cointaglink',
            old_name='newsletters',
            new_name='coins',
        ),
    ]
