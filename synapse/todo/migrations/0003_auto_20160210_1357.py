# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 13:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20160210_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo_list_item',
            name='children',
        ),
        migrations.RemoveField(
            model_name='todo_list_item',
            name='item',
        ),
        migrations.RemoveField(
            model_name='todo_list_item',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='todo_list_item',
            name='sequence_no',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_phone',
        ),
    ]