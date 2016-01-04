# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0006_jurisdiction_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jurisdiction',
            name='bbox',
        ),
        migrations.RemoveField(
            model_name='jurisdiction',
            name='geometry',
        ),
    ]
