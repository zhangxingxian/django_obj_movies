# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-11-26 13:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20181124_2113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tfilm',
            old_name='cate_log_id',
            new_name='cate_log',
        ),
        migrations.RenameField(
            model_name='tfilm',
            old_name='loc_id',
            new_name='loc',
        ),
        migrations.RenameField(
            model_name='tfilm',
            old_name='sub_class_id',
            new_name='sub_class',
        ),
        migrations.RenameField(
            model_name='tfilm',
            old_name='type_id',
            new_name='type',
        ),
    ]
