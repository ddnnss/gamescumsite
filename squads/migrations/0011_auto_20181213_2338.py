# Generated by Django 2.1.4 on 2018-12-13 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0010_auto_20181213_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squad',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='squad_avatars/'),
        ),
    ]