# Generated by Django 2.1.4 on 2018-12-06 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20181206_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steamuser',
            name='discord_id',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]