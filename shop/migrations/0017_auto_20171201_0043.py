# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-01 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20171201_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_picture',
            field=models.ImageField(upload_to='media/blog/%Y'),
        ),
    ]
