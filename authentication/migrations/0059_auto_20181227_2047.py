# Generated by Django 2.1.4 on 2018-12-27 20:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0058_auto_20181227_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steamuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 27, 20, 47, 39, 927276), verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='steamuser',
            name='last_zp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 28, 20, 47, 39, 927276)),
        ),
    ]