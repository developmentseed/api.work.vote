# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20160330_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='city',
            field=models.TextField(blank=True, verbose_name='city', null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='county',
            field=models.TextField(blank=True, verbose_name='county', null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='familiarity_w_technology',
            field=models.IntegerField(verbose_name='How familiar are you with working with computer technology on a scale of 1 to 5? 1 being "not familiar at all" and 5 being "extremely familiar."', default=0),
        ),
        migrations.AlterField(
            model_name='application',
            name='languages',
            field=jsonfield.fields.JSONField(blank=True, verbose_name='What languages do you speak other than English?', null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='familiarity_w_technology',
            field=models.IntegerField(verbose_name='How familiar are you with working with computer technology on a scale of 1 to 10? 1 being "not familiar at all" and 10 being "extremely familiar."', default=0),
        ),
        migrations.AlterField(
            model_name='survey',
            name='languages',
            field=jsonfield.fields.JSONField(blank=True, verbose_name='What languages do you speak other than English?', null=True),
        ),
    ]
