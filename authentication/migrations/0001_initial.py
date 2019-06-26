# Generated by Django 2.1.4 on 2019-06-26 22:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SteamUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('steamid', models.CharField(max_length=17, unique=True, verbose_name='STEAM ID игрока')),
                ('discord_id', models.CharField(blank=True, default=None, max_length=40, null=True, unique=True, verbose_name='DISCORD ID  игрока')),
                ('discord_nickname', models.CharField(blank=True, default=None, max_length=40, null=True, unique=True, verbose_name='DISCORD ник')),
                ('personaname', models.CharField(max_length=255, verbose_name='Ник в стиме')),
                ('nickname', models.SlugField(blank=True, default=None, null=True, verbose_name='Ник в стиме транслит')),
                ('profileurl', models.CharField(max_length=300, verbose_name='Ссылка на профиль')),
                ('avatar', models.CharField(max_length=255, verbose_name='Аватар 3')),
                ('avatarmedium', models.CharField(max_length=255, verbose_name='Аватар 2')),
                ('avatarfull', models.CharField(max_length=255, verbose_name='Аватар 1')),
                ('rank', models.CharField(default='Новичек', max_length=100, verbose_name='Ранг игрока')),
                ('info', models.TextField(blank=True, default='Игрок не указал дополнительных сведений о себе.', verbose_name='Информация')),
                ('wallet', models.IntegerField(default=0, verbose_name='Баланс')),
                ('rating', models.IntegerField(default=1, verbose_name='Рейтинг')),
                ('level', models.IntegerField(default=1, verbose_name='Уровень')),
                ('kills', models.IntegerField(default=0, verbose_name='Убийств')),
                ('deaths', models.IntegerField(default=0, verbose_name='Смертей')),
                ('total_buys_summ', models.IntegerField(default=0, verbose_name='Сумма покупок')),
                ('total_buys_count', models.IntegerField(default=0, verbose_name='Всего покупок')),
                ('vip', models.BooleanField(default=False, verbose_name='ВИП?')),
                ('outlaw', models.BooleanField(default=False, verbose_name='Вне закона?')),
                ('old_player', models.BooleanField(default=False, verbose_name='Старый игрок?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен?')),
                ('is_squad_leader', models.BooleanField(default=False, verbose_name='Лидер отряда?')),
                ('profile_open', models.BooleanField(default=True, verbose_name='Профиль открыт?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Админ?')),
                ('bonus_pack', models.BooleanField(default=False, verbose_name='Выдан бонус-пак?')),
                ('last_zp', models.DateTimeField(default=datetime.datetime(2019, 6, 27, 22, 14, 58, 471414), verbose_name='Последняя ЗП')),
                ('date_joined', models.DateTimeField(default=datetime.datetime(2019, 6, 26, 22, 14, 58, 471414), verbose_name='Дата регистрации')),
                ('last_vizit', models.DateField(default=datetime.date(2019, 6, 26), verbose_name='Последний вход на сайт')),
                ('last_buy', models.DateField(default=datetime.date(2019, 6, 26), verbose_name='Последняя покупка')),
                ('vip_start', models.DateField(default=datetime.date(2019, 6, 26), verbose_name='Начало действия ВИП')),
                ('buys_count', models.IntegerField(default=0, verbose_name='Покупок в течении суток')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_action', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now=True)),
                ('player', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Действие игрока',
                'verbose_name_plural': 'Действия игроков',
            },
        ),
        migrations.CreateModel(
            name='PrivateMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_player_name', models.CharField(max_length=30)),
                ('from_player_name_slug', models.CharField(blank=True, max_length=30)),
                ('from_player_avatar', models.CharField(max_length=255)),
                ('text', models.TextField(default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('to_player', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
