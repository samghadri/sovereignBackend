# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-11-02 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sovereign_box', '0009_auto_20191102_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coins',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='image_file/%Y/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='coins',
            name='image_url_2',
            field=models.ImageField(blank=True, null=True, upload_to='image_file/%Y/', verbose_name='Image'),
        ),
    ]
