# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0012_auto_20160217_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='state_id',
            field=models.IntegerField(unique=True, null=True, verbose_name=b'state ID', blank=True),
        ),
    ]
