# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0021_auto_20180831_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurisdiction',
            name='further_notes',
            field=models.TextField(null=True, verbose_name='Further Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='surveyemail',
            name='send_email',
            field=models.BooleanField(help_text='To edit this field, use the dropdown on the summary view.', default=False, verbose_name='Sent email?'),
        ),
    ]
