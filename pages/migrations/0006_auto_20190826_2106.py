# Generated by Django 2.1.4 on 2019-08-26 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20190826_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='killstat',
            name='killerLocCoordZ',
        ),
        migrations.RemoveField(
            model_name='killstat',
            name='killerLocGameCoordZ',
        ),
        migrations.RemoveField(
            model_name='killstat',
            name='victimLocCoordZ',
        ),
        migrations.RemoveField(
            model_name='killstat',
            name='victimLocGameCoordZ',
        ),
    ]