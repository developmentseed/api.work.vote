# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0007_auto_20160104_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurisdiction',
            name='geometry',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, null=True, verbose_name=b'Jurisdiction Geometry', blank=True),
        ),
    ]
