# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0019_surveyemail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyemail',
            name='jurisdictions',
        ),
        migrations.AddField(
            model_name='surveyemail',
            name='jurisdiction',
            field=smart_selects.db_fields.ChainedManyToManyField(to='jurisdiction.Jurisdiction', chained_field='state', chained_model_field='state'),
        ),
        migrations.AddField(
            model_name='surveyemail',
            name='send_email',
            field=models.BooleanField(help_text='Can only be set to TRUE once this has been saved', verbose_name='Send email?', default=False),
        ),
        migrations.AddField(
            model_name='surveyemail',
            name='state',
            field=models.ForeignKey(to='jurisdiction.State', default=1),
        ),
    ]
