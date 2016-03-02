# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_survey'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 2, 14, 1, 23, 404370, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
