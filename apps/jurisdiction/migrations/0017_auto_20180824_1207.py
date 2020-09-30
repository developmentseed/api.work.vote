# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0016_auto_20180824_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisdiction',
            name='display',
            field=models.CharField(default=b'Y', max_length=255, choices=[(b'Y', b'Display Information'), (b'N', b'No information displayed')]),
        ),
    ]
