# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0010_jurisdiction_voter_registration_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='pollworker_webiste',
            field=models.CharField(max_length=400, null=True, verbose_name=b'State Poll worker website', blank=True),
        ),
    ]
