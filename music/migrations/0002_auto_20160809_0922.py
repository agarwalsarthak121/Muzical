# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-09 09:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='album',
            new_name='album_name',
        ),
    ]
