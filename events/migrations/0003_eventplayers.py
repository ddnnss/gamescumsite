# Generated by Django 2.1.4 on 2018-12-19 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_auto_20181219_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPlayers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Event')),
                ('player', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Участник мероприятия',
                'verbose_name_plural': 'Участники мероприятии',
            },
        ),
    ]
