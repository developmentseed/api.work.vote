# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0004_auto_20151221_0348'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='alpha',
            field=models.CharField(default='a', max_length=2, verbose_name=b'Alpha-2 Code'),
            preserve_default=False,
        ),
    ]
