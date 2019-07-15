# Generated by Django 2.1.4 on 2019-07-15 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_orders_server'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='subitem',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]