# Generated by Django 2.1.4 on 2018-12-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0032_auto_20181220_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatemessages',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='steamuser',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='steamuser',
            name='last_vizit',
            field=models.DateField(auto_now_add=True),
        ),
    ]