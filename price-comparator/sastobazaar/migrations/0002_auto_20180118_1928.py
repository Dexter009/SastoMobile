# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sastobazaar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='darazitem',
            name='category',
        ),
        migrations.AlterField(
            model_name='darazitem',
            name='title',
            field=models.CharField(max_length=512),
        ),
    ]
