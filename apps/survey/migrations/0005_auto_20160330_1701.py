# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_survey_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='familiarity_w_technology',
            field=models.IntegerField(default=0, verbose_name=b'How familiar are you with working with computer technology on a scale of 1 to 5? 1 being "not familiar at all" and 5 being "extremely familiar."'),
        ),
    ]
