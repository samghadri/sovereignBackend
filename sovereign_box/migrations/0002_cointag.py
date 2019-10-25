# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-10-24 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sovereign_box', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoinTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('coins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coin_tags', to='sovereign_box.Coins')),
            ],
        ),
    ]
