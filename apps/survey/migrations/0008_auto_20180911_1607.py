# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_uploadfiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(max_length=250, verbose_name='Response Set Description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('document', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.DeleteModel(
            name='UploadFiles',
        ),
    ]
