# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0011_state_pollworker_webiste'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='pollworker_webiste',
            new_name='pollworker_website',
        ),
    ]
