# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-15 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easyfundraising', '0004_auto_20170315_1456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['pubtime']},
        ),
        migrations.AlterField(
            model_name='item',
            name='author',
            field=models.CharField(max_length=20, verbose_name='\u4f5c\u8005'),
        ),
    ]
