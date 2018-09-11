# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0023_surveyemail_email_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyemail',
            name='email_text',
            field=models.TextField(default='Thank you for your participation in our survey for WorkElections.com. Please click on the link corresponding with the jurisdiction for which you would like to update information.', verbose_name='E-mail text', help_text='This text will be displayed above the survey links.'),
        ),
    ]
