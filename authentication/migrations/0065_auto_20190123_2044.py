# Generated by Django 2.1.4 on 2019-01-23 20:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0064_auto_20190108_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steamuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 20, 44, 9, 936578), verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='steamuser',
            name='last_vizit',
            field=models.DateField(default=datetime.date(2019, 1, 23)),
        ),
        migrations.AlterField(
            model_name='steamuser',
            name='last_zp',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 24, 20, 44, 9, 936578)),
        ),
    ]
