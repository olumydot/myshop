# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-02 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20171202_0352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
    ]