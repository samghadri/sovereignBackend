# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-11-06 21:56
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sovereign_box', '0017_coinoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coins',
            name='image_2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]