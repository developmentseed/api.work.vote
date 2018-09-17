# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0024_auto_20180907_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurisdiction',
            name='student_website',
            field=models.CharField(max_length=400, verbose_name='Website for Student Pollworker Program', blank=True, null=True),
        ),
    ]
