# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-28 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170228_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '教程', 'verbose_name_plural': '教程'},
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.CharField(db_index=True, default='article', max_length=100, verbose_name='网址'),
            preserve_default=False,
        ),
    ]
