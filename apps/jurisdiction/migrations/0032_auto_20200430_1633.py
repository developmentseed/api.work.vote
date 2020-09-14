# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0031_auto_20200427_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurisdiction',
            name='training_note',
            field=models.TextField(blank=True, verbose_name='Training specific notes', null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='jurisdiction_link',
            field=models.ForeignKey(to='jurisdiction.Jurisdiction', verbose_name='link a jurisdiction', null=True, blank=True, on_delete=models.CASCADE),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='jurisdiction_link_text',
            field=models.CharField(blank=True, verbose_name='disambiguation notice', max_length=250, null=True),
        ),
    ]
