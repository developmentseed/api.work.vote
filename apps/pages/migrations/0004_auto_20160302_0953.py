# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.CharField(default=1, unique=True, max_length=250, verbose_name=b"Page's url name"),
            preserve_default=False,
        ),
    ]
