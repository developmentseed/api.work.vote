# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0020_auto_20180830_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveyemail',
            old_name='Jurisdiction',
            new_name='jurisdiction',
        ),
    ]
