# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-28 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170228_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='addr',
            field=models.TextField(max_length=200, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='author',
            name='qq',
            field=models.CharField(max_length=10, verbose_name='QQ'),
        ),
    ]
