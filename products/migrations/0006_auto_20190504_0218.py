# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-05-04 02:18
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190504_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_file),
        ),
    ]
