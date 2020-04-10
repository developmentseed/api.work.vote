# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0027_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisdiction',
            name='registration_status',
            field=models.TextField(blank=True, null=True, verbose_name='Registered in the state OR registered in the jurisdiction? - Input: S or J'),
        ),
        migrations.AlterField(
            model_name='surveyemail',
            name='email_text',
            field=tinymce.models.HTMLField(verbose_name='E-mail text', default='Thank you for your participation in our survey for WorkElections.com. Please click on the link corresponding with the jurisdiction for which you would like to update information.', help_text='This text will be displayed above the survey links.'),
        ),
        migrations.AlterField(
            model_name='surveyemail',
            name='name',
            field=models.CharField(verbose_name='Email label', help_text='Used as display name and as email subject line.', max_length=250),
        ),
    ]
