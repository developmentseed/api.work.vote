# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20160302_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Post content', null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='is_active',
            field=models.BooleanField(verbose_name='Page is published?', default=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.CharField(verbose_name="Page's url name", max_length=250, serialize=False, primary_key=True, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(verbose_name='Post Title', max_length=250),
        ),
    ]
