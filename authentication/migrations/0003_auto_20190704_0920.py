# Generated by Django 2.1.4 on 2019-07-04 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20190704_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steamuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 4, 9, 20, 55, 794657), verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='steamuser',
            name='last_zp',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 5, 9, 20, 55, 794657), verbose_name='Последняя ЗП'),
        ),
    ]
