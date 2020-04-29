# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0030_auto_20200422_1753'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jurisdiction',
            old_name='city_model',
            new_name='jurisdiction_link',
        ),
        migrations.RenameField(
            model_name='jurisdiction',
            old_name='city_sub',
            new_name='jurisdiction_link_text',
        ),
    ]
