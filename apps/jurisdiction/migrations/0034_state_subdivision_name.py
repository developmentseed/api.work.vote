# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0033_trusted_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='subdivision_name',
            field=models.CharField(default='County', max_length=250, verbose_name='Subdivision Name'),
        ),
    ]
