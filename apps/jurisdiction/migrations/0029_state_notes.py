# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0028_auto_20200410_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='notes',
            field=models.TextField(verbose_name='Notes', blank=True, null=True),
        ),
    ]
