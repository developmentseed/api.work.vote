# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0008_jurisdiction_geometry'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name=b'Wheter state is active'),
        ),
    ]
