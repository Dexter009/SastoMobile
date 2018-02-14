# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sastobazaar', '0002_auto_20180118_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='NepBayItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=512)),
                ('image', models.CharField(max_length=344)),
                ('url', models.CharField(max_length=324)),
                ('price', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=322)),
            ],
        ),
    ]
