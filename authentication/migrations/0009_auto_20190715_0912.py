# Generated by Django 2.1.4 on 2019-07-15 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20190714_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steamuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 15, 9, 12, 3, 642798), verbose_name='Дата регистрации'),
        ),
        migrations.AlterField(
            model_name='steamuser',
            name='last_buy',
            field=models.DateField(default=datetime.date(2019, 7, 15), verbose_name='Последняя покупка'),
        ),
        migrations.AlterField(
            model_name='steamuser',
            name='last_vizit',
            field=models.DateField(default=datetime.date(2019, 7, 15), verbose_name='Последний вход на сайт'),
        ),
        migrations.AlterField(
            model_name='steamuser',
            name='last_zp',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 16, 9, 12, 3, 642798), verbose_name='Последняя ЗП'),
        ),
        migrations.AlterField(
            model_name='steamuser',
            name='vip_start',
            field=models.DateField(default=datetime.date(2019, 7, 15), verbose_name='Начало действия ВИП'),
        ),
    ]
