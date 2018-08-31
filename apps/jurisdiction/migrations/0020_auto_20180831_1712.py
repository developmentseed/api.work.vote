# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0019_surveyemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyemail',
            name='recipients',
            field=models.TextField(verbose_name='List of emails', help_text='Use commas, semicolons or line breaks to separate emails. Do not enter e-mail addresses containing those special characters.'),
        ),
    ]
