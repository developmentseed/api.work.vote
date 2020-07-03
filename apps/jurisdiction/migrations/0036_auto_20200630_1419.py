# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0035_jurisdiction_city_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisdiction',
            name='city_label',
            field=models.CharField(default='City', blank=True, verbose_name='Label for local government unit (if city)', max_length=250),
        ),
    ]
