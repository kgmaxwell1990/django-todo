# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 12:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoitem', '0002_auto_20171108_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitems',
            old_name='completed',
            new_name='done',
        ),
    ]
