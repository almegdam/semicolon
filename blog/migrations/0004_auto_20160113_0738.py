# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160112_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='images'),
        ),
    ]
