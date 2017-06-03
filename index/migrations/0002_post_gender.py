# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-02 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=0, max_length=2),
            preserve_default=False,
        ),
    ]