# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0015_jurisdiction_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisdiction',
            name='display',
            field=models.CharField(default=b'Y', max_length=1, null=True, choices=[(b'Y', b'Display Information'), (b'N', b'No information displayed')]),
        ),
    ]
