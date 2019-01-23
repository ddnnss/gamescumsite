# Generated by Django 2.1.4 on 2019-01-23 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20181221_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliceStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obez', models.IntegerField(default=0, verbose_name='Обезврежено')),
                ('victim', models.IntegerField(default=0, verbose_name='Жертвы')),
                ('izyato', models.IntegerField(default=0, verbose_name='Изъято')),
            ],
            options={
                'verbose_name': 'Полицейская стата',
                'verbose_name_plural': 'Полицейская стата',
            },
        ),
    ]
