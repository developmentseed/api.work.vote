# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0013_state_state_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='state_id',
        ),
    ]
