# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DarazItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.CharField(max_length=344)),
                ('url', models.CharField(max_length=324)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=322)),
                ('price', models.CharField(max_length=32)),
                ('category', models.CharField(max_length=32)),
            ],
        ),
    ]
