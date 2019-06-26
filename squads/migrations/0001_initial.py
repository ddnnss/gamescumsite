# Generated by Django 2.1.4 on 2019-06-26 22:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SectorWars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('war_date', models.DateTimeField(default=None, null=True)),
                ('owner_agreed', models.BooleanField(null=True)),
                ('for_bot_enemy_squad_name', models.CharField(blank=True, max_length=50)),
                ('for_bot_sector_name', models.CharField(blank=True, max_length=50)),
                ('for_bot_owner_name', models.CharField(blank=True, max_length=50)),
                ('for_bot_owner_discord_id', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Война за сектор',
                'verbose_name_plural': 'Война за секторы',
            },
        ),
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('name_slug', models.SlugField(blank=True, unique=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='squad_avatars/')),
                ('balance', models.IntegerField(blank=True, default=0)),
                ('level', models.IntegerField(blank=True, default=1)),
                ('rating', models.IntegerField(blank=True, default=1)),
                ('info', models.TextField(blank=True, default='Дополнительных сведений об отряде не предоставлено.', null=True)),
                ('battles_wins', models.IntegerField(blank=True, default=0)),
                ('battles_loose', models.IntegerField(blank=True, default=0)),
                ('vip', models.BooleanField(default=False)),
                ('recruting', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2019, 6, 26, 22, 14, 58, 479392))),
                ('leader', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Отряд',
                'verbose_name_plural': 'Отряды',
            },
        ),
        migrations.CreateModel(
            name='SquadMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.IntegerField(blank=True, default=0)),
                ('player', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('squad', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='squads.Squad')),
            ],
            options={
                'verbose_name': 'Участник отряда',
                'verbose_name_plural': 'Участник отряда',
            },
        ),
        migrations.CreateModel(
            name='SquadRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime(2019, 6, 26, 22, 14, 58, 480390))),
                ('player', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('squad', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='squads.Squad')),
            ],
            options={
                'verbose_name': 'Заявка в отряд',
                'verbose_name_plural': 'Заявки в отряды',
            },
        ),
        migrations.CreateModel(
            name='SquadSectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('income', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('in_war', models.BooleanField(default=False)),
                ('own', models.DateTimeField(default=datetime.datetime(2019, 6, 26, 22, 14, 58, 481387))),
                ('last_pay', models.DateTimeField(default=datetime.datetime(2019, 6, 26, 22, 14, 58, 481387))),
                ('squad', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='squads.Squad')),
            ],
            options={
                'verbose_name': 'Сектор',
                'verbose_name_plural': 'Сектора',
            },
        ),
        migrations.CreateModel(
            name='SquadWear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('spawn_info', models.TextField(default='Тут можно указать команды спавна')),
                ('image', models.ImageField(null=True, upload_to='squad_avatars/')),
                ('for_vip', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Форма',
                'verbose_name_plural': 'Формы',
            },
        ),
        migrations.AddField(
            model_name='squad',
            name='wear',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='squads.SquadWear'),
        ),
        migrations.AddField(
            model_name='sectorwars',
            name='enemy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='squads.Squad'),
        ),
        migrations.AddField(
            model_name='sectorwars',
            name='sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='squads.SquadSectors'),
        ),
    ]
