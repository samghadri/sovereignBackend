# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-10-24 15:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sovereign_box', '0002_cointag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cointag',
            name='coins',
        ),
    ]