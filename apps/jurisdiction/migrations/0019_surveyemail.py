# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0018_auto_20180830_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=250, verbose_name='Email label')),
                ('recipients', models.TextField(help_text='Use comma, semicolon or line break to separate emails', verbose_name='List of emails')),
                ('jurisdictions', models.ManyToManyField(to='jurisdiction.Jurisdiction', verbose_name='Send links to all these jurisdictions:')),
            ],
        ),
    ]
