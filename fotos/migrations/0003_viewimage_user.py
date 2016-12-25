# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-17 05:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fotos', '0002_auto_20160816_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewimage',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
