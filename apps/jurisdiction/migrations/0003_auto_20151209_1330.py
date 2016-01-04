# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0002_auto_20151208_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurisdiction',
            name='notes',
            field=models.TextField(null=True, verbose_name=b'Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='registration_status',
            field=models.TextField(null=True, verbose_name=b'Registered in the state OR registered in the jurisdiction?- Input: S or J', blank=True),
        ),
    ]
