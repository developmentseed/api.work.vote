# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0024_auto_20180907_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zipcode',
            fields=[
                ('code', models.CharField(primary_key=True, max_length=5, verbose_name='Zip Code', serialize=False)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, verbose_name='zipcode Geometry', srid=4326)),
            ],
        ),
        migrations.AlterField(
            model_name='state',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Whether state is active'),
        ),
        migrations.AddField(
            model_name='zipcode',
            name='state',
            field=models.ForeignKey(to='jurisdiction.State'),
        ),
    ]
