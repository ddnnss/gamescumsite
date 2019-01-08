# Generated by Django 2.1.4 on 2019-01-07 23:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0037_auto_20190107_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectorwars',
            name='owner_agreed',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='squad',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 7, 23, 18, 43, 137032)),
        ),
        migrations.AlterField(
            model_name='squadrequests',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 7, 23, 18, 43, 138029)),
        ),
        migrations.AlterField(
            model_name='squadsectors',
            name='last_pay',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 7, 23, 18, 43, 138029)),
        ),
        migrations.AlterField(
            model_name='squadsectors',
            name='own',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 7, 23, 18, 43, 138029)),
        ),
    ]
