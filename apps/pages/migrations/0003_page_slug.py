# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20160229_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.CharField(max_length=250, null=True, verbose_name=b"Page's url name", blank=True),
        ),
    ]
