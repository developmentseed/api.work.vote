# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jurisdiction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name=b'Jurisdiction Name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('obtained_at', models.DateField(null=True, verbose_name=b'Date obtained', blank=True)),
                ('website', models.CharField(max_length=400, null=True, verbose_name=b'info website', blank=True)),
                ('application', models.CharField(max_length=400, null=True, verbose_name=b'online application', blank=True)),
                ('telephone', models.CharField(max_length=250, null=True, verbose_name=b'telephone', blank=True)),
                ('email', models.CharField(max_length=250, null=True, verbose_name=b'email', blank=True)),
                ('office_address', models.CharField(max_length=250, null=True, verbose_name=b'office address', blank=True)),
                ('mailing_address', models.CharField(max_length=250, null=True, verbose_name=b'mailing address (if different)', blank=True)),
                ('how_obtained', models.CharField(max_length=250, null=True, verbose_name=b'how data obtained', blank=True)),
                ('registration_status', models.CharField(max_length=250, null=True, verbose_name=b'Registered in the state OR registered in the jurisdiction? - Input: S or J', blank=True)),
                ('pre_registration', models.CharField(max_length=250, null=True, verbose_name=b"If pre-registration is available, is it required for 16/17 yo's? - Input: Y or N", blank=True)),
                ('minimum_age', models.CharField(max_length=250, null=True, verbose_name=b'Minimum age - Input: ##', blank=True)),
                ('high_school_student', models.CharField(max_length=250, null=True, verbose_name=b'Can high school students work? - Input: Y or N', blank=True)),
                ('hours_start', models.CharField(max_length=250, null=True, verbose_name=b'Hours start', blank=True)),
                ('hours_end', models.CharField(max_length=250, null=True, verbose_name=b'Hours end', blank=True)),
                ('full_day_req', models.CharField(max_length=250, null=True, verbose_name=b'Full Day required - Input: Y or N', blank=True)),
                ('split_days_allowed', models.CharField(max_length=250, null=True, verbose_name=b'If split days are allowed, must one find a buddy? Input: Y or N', blank=True)),
                ('compensation', models.CharField(max_length=250, null=True, verbose_name=b'Pay/compensation for the day - Input: Total amount OR hourly rate OR a range from min to max if the pay varies based on position.', blank=True)),
                ('interview', models.CharField(max_length=250, null=True, verbose_name=b'Interview requirement - Input: Y or N', blank=True)),
                ('training', models.CharField(max_length=250, null=True, verbose_name=b'Training - Input: Y or N', blank=True)),
                ('complete_training', models.CharField(max_length=250, null=True, verbose_name=b'Complete training for each election? - Input: Y or N', blank=True)),
                ('post_training_exam', models.CharField(max_length=250, null=True, verbose_name=b'Pass a post-training exam or assessment - Input: Y or N', blank=True)),
                ('must_have_email', models.CharField(max_length=250, null=True, verbose_name=b'Must have an email address and access to a computer and internet - Input: Y or N', blank=True)),
                ('candidate_prohibition', models.CharField(max_length=250, null=True, verbose_name=b'Prohibition on being a candidate or related to a candidate - Y or N', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name=b'State')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='jurisdiction',
            name='state',
            field=models.ForeignKey(to='jurisdiction.State',on_delete=models.PROTECT),
        ),
    ]
