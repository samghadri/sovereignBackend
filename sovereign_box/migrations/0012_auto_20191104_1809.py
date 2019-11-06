# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-11-04 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sovereign_box', '0011_auto_20191102_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='coins',
            name='certification_code',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='coins',
            name='grading_company',
            field=models.CharField(blank=True, choices=[('P', 'PCGS'), ('N', 'NGC')], max_length=1, null=True),
        ),
    ]