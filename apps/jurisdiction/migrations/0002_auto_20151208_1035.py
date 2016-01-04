# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisdiction',
            name='candidate_prohibition',
            field=models.TextField(null=True, verbose_name=b'Prohibition on being a candidate or related to a candidate - Y or N', blank=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='compensation',
            field=models.TextField(null=True, verbose_name=b'Pay/compensation for the day - Input: Total amount OR hourly rate OR a range from min to max if the pay varies based on position.', blank=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='complete_training',
            field=models.TextField(null=True, verbose_name=b'Complete training for each election? - Input: Y or N', blank=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='full_day_req',
            field=models.TextField(null=True, verbose_name=b'Full Day required - Input: Y or N', blank=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='high_school_student',
            field=models.TextField(null=True, verbose_name=b'Can high school students work? - Input: Y or N', blank=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='how_obtained',
            field=models.TextField(null=True, verbose_name=b'how data obtained', blank=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='interview',
            field=models.TextField(null=True, verbose_name=b'Interview requirement - Input: Y or N', blank=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='mailing_address',
            field=models.TextField(null=True, verbose_name=b'mailing address (if different)', blank=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='must_have_email',
            field=models.TextField(null=True, verbose_name=b'Must have an email address and access to a computer and internet - Input: Y or N', blank=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='office_address',
            field=models.TextField(null=True, verbose_name=b'office address', blank=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='post_training_exam',
            field=models.TextField(null=True, verbose_name=b'Pass a post-training exam or assessment - Input: Y or N', blank=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='pre_registration',
            field=models.TextField(null=True, verbose_name=b"If pre-registration is available, is it required for 16/17 yo's? - Input: Y or N", blank=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='registration_status',
            field=models.TextField(null=True, verbose_name=b'Registered in the state OR registered in the jurisdiction? - Input: S or J', blank=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='split_days_allowed',
            field=models.TextField(null=True, verbose_name=b'If split days are allowed, must one find a buddy? Input: Y or N', blank=True),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='training',
            field=models.TextField(null=True, verbose_name=b'Training - Input: Y or N', blank=True),
        ),
    ]
