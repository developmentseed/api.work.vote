# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0029_state_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurisdiction',
            name='city_model',
            field=models.ForeignKey(blank=True, null=True, to='jurisdiction.Jurisdiction'),
        ),
        migrations.AddField(
            model_name='jurisdiction',
            name='city_sub',
            field=models.CharField(verbose_name='text for the message in the sub', max_length=250, blank=True, null=True),
        ),
    ]
