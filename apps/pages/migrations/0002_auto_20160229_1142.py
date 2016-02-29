# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=tinymce.models.HTMLField(null=True, verbose_name=b'Post content', blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name=b'Page is published?'),
        ),
    ]
