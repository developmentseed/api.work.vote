# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0022_auto_20180904_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyemail',
            name='email_text',
            field=models.TextField(verbose_name='E-mail text', help_text='What do you want the e-mail to say?', default='Thank you for your participation in our survey for WorkElections.com. Please click on the link corresponding with the jurisdiction for which you would like to update information.'),
        ),
    ]
