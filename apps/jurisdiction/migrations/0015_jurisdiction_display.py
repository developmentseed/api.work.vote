# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0014_remove_state_state_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurisdiction',
            name='display',
            field=models.CharField(default=b'Y', max_length=255, choices=[(b'Y', b'Display Information'), (b'N', b'No information displayed')]),
        ),
    ]
