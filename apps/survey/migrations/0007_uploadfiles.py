# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20180830_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('description', models.CharField(verbose_name='Post Title', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('document', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
