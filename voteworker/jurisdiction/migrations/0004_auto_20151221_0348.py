# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0003_auto_20151209_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurisdiction',
            name='bbox',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True, verbose_name=b'Bounding Box', blank=True),
        ),
        migrations.AddField(
            model_name='jurisdiction',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True, verbose_name=b'Jurisdiction Geometry', blank=True),
        ),
    ]
