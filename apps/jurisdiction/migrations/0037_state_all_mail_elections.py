# Generated by Django 3.1.1 on 2020-09-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdiction', '0036_auto_20200630_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='all_mail_elections',
            field=models.BooleanField(default=False, verbose_name='Whether State has All Mail Elections'),
        ),
    ]
