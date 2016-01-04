# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0005_state_alpha'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurisdiction',
            name='city',
            field=models.BooleanField(default=False, verbose_name=b'Whether the jurisdiction is a city'),
        ),
    ]
