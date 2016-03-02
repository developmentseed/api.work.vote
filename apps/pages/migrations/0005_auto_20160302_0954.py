# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20160302_0953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='id',
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.CharField(max_length=250, unique=True, serialize=False, verbose_name=b"Page's url name", primary_key=True),
        ),
    ]
