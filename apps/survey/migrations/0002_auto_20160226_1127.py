# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0014_remove_state_state_id'),
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='city',
            field=models.TextField(null=True, verbose_name=b'city', blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='county',
            field=models.TextField(null=True, verbose_name=b'county', blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='jurisdiction',
            field=models.ForeignKey(related_name='app_jurisdiction', default=1, to='jurisdiction.Jurisdiction', on_delete=models.CASCADE),
            preserve_default=False,
        ),
    ]
