# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0009_state_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurisdiction',
            name='voter_registration_url',
            field=models.CharField(max_length=300, null=True, verbose_name=b'Website for online voter regisration', blank=True),
        ),
    ]
