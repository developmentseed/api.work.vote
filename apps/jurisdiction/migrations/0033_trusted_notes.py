# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0032_auto_20200430_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jurisdiction',
            name='notes',
        ),
        migrations.AddField(
            model_name='jurisdiction',
            name='trusted_notes',
            field=tinymce.models.HTMLField(verbose_name='Notes (trusted content rendered without HTML escaping)', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='further_notes',
            field=models.TextField(verbose_name='Further Notes (populated from survey responses)', null=True, blank=True),
        ),
    ]
