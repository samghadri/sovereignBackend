# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-11-02 23:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sovereign_box', '0010_auto_20191102_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coins',
            old_name='image_url',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='coins',
            old_name='image_url_2',
            new_name='image_2',
        ),
    ]
