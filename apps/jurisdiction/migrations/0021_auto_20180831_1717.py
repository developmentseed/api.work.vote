# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0020_auto_20180831_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyemail',
            name='jurisdictions',
        ),
        migrations.AddField(
            model_name='surveyemail',
            name='jurisdiction',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_model_field='state', chained_field='state', to='jurisdiction.Jurisdiction'),
        ),
        migrations.AddField(
            model_name='surveyemail',
            name='send_email',
            field=models.BooleanField(help_text='Can only be set to TRUE once this has been saved', verbose_name='Sent email?', default=False),
        ),
        migrations.AddField(
            model_name='surveyemail',
            name='state',
            field=models.ForeignKey(to='jurisdiction.State', default=1, on_delete=models.CASCADE),
        ),
    ]
