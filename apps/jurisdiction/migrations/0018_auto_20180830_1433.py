# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0017_auto_20180824_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisdiction',
            name='application',
            field=models.CharField(blank=True, verbose_name='online application', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='candidate_prohibition',
            field=models.TextField(blank=True, verbose_name='Prohibition on being a candidate or related to a candidate - Y or N', null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='city',
            field=models.BooleanField(verbose_name='Whether the jurisdiction is a city', default=False),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='compensation',
            field=models.TextField(blank=True, verbose_name='Pay/compensation for the day - Input: Total amount OR hourly rate OR a range from min to max if the pay varies based on position.', null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='complete_training',
            field=models.TextField(blank=True, verbose_name='Complete training for each election? - Input: Y or N', null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='display',
            field=models.CharField(max_length=1, choices=[('Y', 'Display Information'), ('N', 'No information displayed')], default='Y'),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='email',
            field=models.CharField(blank=True, verbose_name='email', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='full_day_req',
            field=models.TextField(blank=True, verbose_name='Full Day required - Input: Y or N', null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='geometry',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, verbose_name='Jurisdiction Geometry', srid=4326, null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='high_school_student',
            field=models.TextField(blank=True, verbose_name='Can high school students work? - Input: Y or N', null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='hours_end',
            field=models.CharField(blank=True, verbose_name='Hours end', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='hours_start',
            field=models.CharField(blank=True, verbose_name='Hours start', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='how_obtained',
            field=models.TextField(blank=True, verbose_name='how data obtained', null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='interview',
            field=models.TextField(blank=True, verbose_name='Interview requirement - Input: Y or N', null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='mailing_address',
            field=models.TextField(blank=True, verbose_name='mailing address (if different)', null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='minimum_age',
            field=models.CharField(blank=True, verbose_name='Minimum age - Input: ##', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='must_have_email',
            field=models.TextField(blank=True, verbose_name='Must have an email address and access to a computer and internet - Input: Y or N', null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='name',
            field=models.CharField(verbose_name='Jurisdiction Name', max_length=250),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes', null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='obtained_at',
            field=models.DateField(blank=True, verbose_name='Date obtained', null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='office_address',
            field=models.TextField(blank=True, verbose_name='office address', null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='post_training_exam',
            field=models.TextField(blank=True, verbose_name='Pass a post-training exam or assessment - Input: Y or N', null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='pre_registration',
            field=models.TextField(blank=True, verbose_name="If pre-registration is available, is it required for 16/17 yo's? - Input: Y or N", null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='registration_status',
            field=models.TextField(blank=True, verbose_name='Registered in the state OR registered in the jurisdiction?- Input: S or J', null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='split_days_allowed',
            field=models.TextField(blank=True, verbose_name='If split days are allowed, must one find a buddy? Input: Y or N', null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='telephone',
            field=models.CharField(blank=True, verbose_name='telephone', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='training',
            field=models.TextField(blank=True, verbose_name='Training - Input: Y or N', null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='voter_registration_url',
            field=models.CharField(blank=True, verbose_name='Website for online voter regisration', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='website',
            field=models.CharField(blank=True, verbose_name='info website', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='alpha',
            field=models.CharField(verbose_name='Alpha-2 Code', max_length=2),
        ),
        migrations.AlterField(
            model_name='state',
            name='is_active',
            field=models.BooleanField(verbose_name='Wheter state is active', default=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(verbose_name='State', max_length=250),
        ),
        migrations.AlterField(
            model_name='state',
            name='pollworker_website',
            field=models.CharField(blank=True, verbose_name='State Poll worker website', max_length=400, null=True),
        ),
    ]
