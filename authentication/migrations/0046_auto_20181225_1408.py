# Generated by Django 2.1.4 on 2018-12-25 11:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0045_auto_20181223_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='steamuser',
            name='bonus_pack',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='steamuser',
            name='total_buys_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='steamuser',
            name='total_buys_summ',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='steamuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 25, 11, 8, 57, 443626, tzinfo=utc), verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='steamuser',
            name='last_vizit',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 25, 11, 8, 57, 443626, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='steamuser',
            name='last_zp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 26, 11, 8, 57, 443626, tzinfo=utc)),
        ),
    ]
