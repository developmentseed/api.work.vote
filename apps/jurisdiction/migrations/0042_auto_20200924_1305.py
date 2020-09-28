# Generated by Django 3.1.1 on 2020-09-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0041_auto_20200924_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jurisdiction',
            name='under_eighteen_requirments',
        ),
        migrations.AddField(
            model_name='jurisdiction',
            name='under_eighteen_req',
            field=models.TextField(blank=True, null=True, verbose_name='special under 18 requirements'),
        ),
    ]
