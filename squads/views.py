from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from squads.forms import *
from squads.models import *
from authentication.models import *
# from datetime import datetime
import datetime
from django.core.files.storage import FileSystemStorage
import csv
import os
from django.conf import settings
import bot_settings
from discord_webhook import DiscordWebhook, DiscordEmbed



def create_squad(request):
    if request.POST:

        if request.POST.get('update'):
            print('upadting')
            squad = Squad.objects.get(leader_id=request.user.id)
            print(request.POST)
            squad_form = UpdateSquadForm(request.POST, request.FILES, instance=squad)
            if squad_form.is_valid():
                squad_form.save()
                return HttpResponseRedirect('/profile/' + request.user.nickname +'#squad')
        else:
            squad_form = CreateSquadForm(request.POST, request.FILES)
            if squad_form.is_valid():
                instance = Squad(avatar=request.FILES['avatar'])
                squad_form.save()
                request.user.wallet -= 1000
                request.user.save(force_update=True)
                return HttpResponseRedirect('/profile/' + request.user.nickname +'#squad')

    return HttpResponseRedirect('/profile/' + request.user.nickname)


def buy_sector(request):
    squad = Squad.objects.get(leader=request.user)
    sectors_count = SquadSectors.objects.filter(squad=squad).count()
    sector_to_buy = SquadSectors.objects.get(id=int(request.GET.get('s')))
    if sector_to_buy.price <= squad.balance:
        if squad.level == 1:
            if sectors_count < 1:
                squad.balance -= sector_to_buy.price
                sector_to_buy.squad_id = squad.id
                sector_to_buy.own = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                squad.save(force_update=True)
                sector_to_buy.save(force_update=True)
                messages.add_message(request, messages.SUCCESS, 'СЕКТОР ПРИОБРЕТЕН!')
            else:
                messages.add_message(request, messages.INFO, 'На данном уровне отряда можно иметь только 1 сектор!')
        if squad.level == 2:
            if sectors_count < 2:
                squad.balance -= sector_to_buy.price
                sector_to_buy.squad_id = squad.id
                sector_to_buy.own = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                squad.save(force_update=True)
                sector_to_buy.save(force_update=True)
                messages.add_message(request, messages.SUCCESS, 'СЕКТОР ПРИОБРЕТЕН!')
            else:
                messages.add_message(request, messages.INFO, 'На данном уровне отряда можно иметь только 2 сектора!')
        if squad.level == 3:
            if sectors_count < 3:
                squad.balance -= sector_to_buy.price
                sector_to_buy.squad_id = squad.id
                sector_to_buy.own = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                squad.save(force_update=True)
                sector_to_buy.save(force_update=True)
                messages.add_message(request, messages.SUCCESS, 'СЕКТОР ПРИОБРЕТЕН!')
            else:
                messages.add_message(request, messages.INFO, 'На данном уровне отряда можно иметь только 3 сектора!')

        if squad.level == 4:
            if sectors_count < 4:
                squad.balance -= sector_to_buy.price
                sector_to_buy.squad_id = squad.id
                sector_to_buy.own = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                squad.save(force_update=True)
                sector_to_buy.save(force_update=True)
                messages.add_message(request, messages.SUCCESS, 'СЕКТОР ПРИОБРЕТЕН!')
            else:
                messages.add_message(request, messages.INFO, 'На данном уровне отряда можно иметь только 4 сектора!')

        if squad.level == 5:
            if sectors_count < 5:
                squad.balance -= sector_to_buy.price
                sector_to_buy.squad_id = squad.id
                sector_to_buy.own = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                squad.save(force_update=True)
                sector_to_buy.save(force_update=True)
                messages.add_message(request, messages.SUCCESS, 'СЕКТОР ПРИОБРЕТЕН!')
            else:
                messages.add_message(request, messages.INFO, 'У отряда максимальное количество покупаемых секторов!')

    else:
        messages.add_message(request, messages.WARNING, 'Нехватает денег для приобретения сектора!')

    return HttpResponseRedirect('/squad/#sectors_map')


def add_to_balance(request):

    if request.POST:
        player = request.user
        if player.wallet >= int(request.POST.get('rc_amount')) and int(request.POST.get('rc_amount')) >= 500:
            squad = Squad.objects.get(id=request.POST.get('squad_id'))
            squad_member = SquadMembers.objects.get(player=player.id)
            squad_member.income += int(request.POST.get('rc_amount'))
            squad_member.save(force_update=True)
            player.wallet -= int(request.POST.get('rc_amount'))
            player.rating += 5
            player.save(force_update=True)
            squad.balance += int(request.POST.get('rc_amount'))
            squad.save(force_update=True)
            messages.add_message(request, messages.SUCCESS,
                                     'Баланс отряда успешно пополнен на ' + request.POST.get('rc_amount') + ' RC')
        else:
            messages.add_message(request, messages.WARNING, 'Минимальная сумма пополнения 500 RC!')


        return HttpResponseRedirect('/profile/' + request.user.nickname)

def show_squads(request):
    page_title = 'ОТРЯДЫ И ИГРОКИ СЕРВЕРА'
    print('show_squads')
    squad_active = 'active'
    squads = Squad.objects.all()
    players = SteamUser.objects.filter( is_active=True).order_by('-rating')
    player = request.user
    print(player.id)
    req_disct = []
    sectors_a = SquadSectors.objects.filter(name__startswith='a').order_by('-name')
    sectors_b = SquadSectors.objects.filter(name__startswith='b').order_by('-name')
    sectors_c = SquadSectors.objects.filter(name__startswith='c').order_by('-name')
    sectors_d = SquadSectors.objects.filter(name__startswith='d').order_by('-name')
    wars = SectorWars.objects.all()
    try:
        squad_requests = SquadRequests.objects.filter(player_id=player.id)
    except:
        squad_requests = None
    if squad_requests:
        for req in squad_requests:
            req_disct.append(req.squad.id)
        print(req_disct)

    return render(request, 'squads/index.html', locals())

def join_request(request,name_slug):
    try:
        squad = Squad.objects.get(name_slug=name_slug)
    except:
        squad = None

    if squad:
        if request.user.id is not None:
            new_log = Logs.objects.create(player_id=request.user.id,
                                          player_action='Подана заявка в отряд ' + squad.name)
            new_log.save()
            new_request = SquadRequests.objects.create(squad_id=squad.id, player_id=request.user.id)
            new_request.save()
            new_message = PrivateMessages.objects.create(to_player_id=squad.leader.id,
                                                         from_player_name=request.user.personaname,
                                                         from_player_name_slug=request.user.nickname,
                                                         from_player_avatar=str(request.user.avatar),
                                                         text='Привет, хочу вступить в твой отряд!')
            new_message.save()
            return HttpResponseRedirect('/squad/')
        else:

            return HttpResponseRedirect('/squad/')
    else:
        new_log = Logs.objects.create(player_id=request.user.id,
                                      player_action='Подана заявка в несуществующий отряд ')
        new_log.save()
        return HttpResponseRedirect('/squad/')




def confirm_request(request):
    squad = Squad.objects.get(leader=request.user)
    members_count = SquadMembers.objects.filter(squad=squad).count()
    if squad.level == 1:
        if members_count < 3:
            pass
        else:
            messages.add_message(request, messages.INFO, 'На данном уровне отряда можно иметь только 3 человека в отряде!')
            squad.recruting = False
            squad.save(force_update=True)
    if squad.level == 2:
        if members_count < 4:
            pass
        else:
            messages.add_message(request, messages.INFO,
                                 'На данном уровне отряда можно иметь только 4 человека в отряде!')
            squad.recruting = False
            squad.save(force_update=True)
    if squad.level == 3:
        if members_count < 5:
            pass
        else:
            messages.add_message(request, messages.INFO,
                                 'На данном уровне отряда можно иметь только 5 человек в отряде!')
            squad.recruting = False
            squad.save(force_update=True)

    if squad.level == 4:
        if members_count < 6:
            pass
        else:
            messages.add_message(request, messages.INFO,
                                 'На данном уровне отряда можно иметь только 6 человек в отряде!')
            squad.recruting = False
            squad.save(force_update=True)

    if squad.level == 5:
        if members_count < 7:
            pass
        else:
            messages.add_message(request, messages.INFO,
                                 'В отряда можно иметь 7 человек максимум!')
            squad.recruting = False
            squad.save(force_update=True)

    if squad.recruting:
        req_user = SteamUser.objects.get(nickname=request.GET.get('name'))
        req_squad = SquadMembers.objects.create(squad_id=squad.id, player_id=req_user.id)
        req_squad.save()
        player_req = SquadRequests.objects.filter(player_id=req_user.id)
        player_req.delete()
    return HttpResponseRedirect('/profile/' + request.user.nickname)

def reject_request(request):
    req = SquadRequests.objects.get(id=int(request.GET.get('r_id')))
    squad = req.squad
    if request.user.id == squad.leader.id:
        req.delete()
        new_message = PrivateMessages.objects.create(to_player_id=req.player.id,
                                                     from_player_name=request.user.personaname,
                                                     from_player_name_slug=request.user.nickname,
                                                     from_player_avatar=str(request.user.avatar),
                                                     text='Заявка на вступление отклонена')
        new_message.save()
    return HttpResponseRedirect('/profile/' + request.user.nickname)

def kick_player(request,nickname):
    squad_member = SquadMembers.objects.get(player__nickname=nickname)
    squad = squad_member.squad
    if request.user.id == squad.leader.id:
        squad_member.delete()
        new_message = PrivateMessages.objects.create(to_player_id=squad_member.player.id,
                                                     from_player_name=request.user.personaname,
                                                     from_player_name_slug=request.user.nickname,
                                                     from_player_avatar=str(request.user.avatar),
                                                     text='Привет, ты был кикнут из отряда.')
        new_message.save()
    return HttpResponseRedirect('/profile/' + request.user.nickname)


def level_up(request):
    squad = Squad.objects.get(leader=request.user)

    if squad.level == 1:
        if squad.balance >= 1000:
            squad.balance -= 1000
            squad.level = 2
            squad.save(force_update=True)
    elif squad.level == 2:
        if squad.balance >= 3000:
            squad.balance -= 3000
            squad.level = 3
            squad.recruting = True
            squad.save(force_update=True)
    elif squad.level == 3:
        if squad.balance >= 5000:
            squad.balance -= 5000
            squad.level = 4
            squad.recruting = True
            squad.save(force_update=True)
    elif squad.level == 4:
        if squad.balance >= 10000:
            squad.balance -= 10000
            squad.level = 5
            squad.recruting = True
            squad.save(force_update=True)
    elif squad.level == 5:
        if squad.balance >= 15000:
            squad.balance -= 15000
            squad.level = 6
            squad.recruting = True
            squad.vip = True
            squad.save(force_update=True)

    messages.add_message(request, messages.INFO,
                         'Уровень отряда успешно повышен. Открыты новые возможности!')


    return HttpResponseRedirect('/profile/' + request.user.nickname)

def delete_squad(request):
    squad_to_delete = Squad.objects.get(leader=request.user)
    # SquadMembers.objects.filter(squad=squad_to_delete).delete()
    # SquadSectors.objects.filter(squad=squad_to_delete).update(squad=None)
    # SquadRequests.objects.filter(squad=squad_to_delete).delete()
    # SectorWars.objects.filter(enemy=squad_to_delete).delete()
    request.user.is_squad_leader = False
    request.user.rank = 'Бывалый'
    request.user.save(force_update=True)
    squad_to_delete.delete()

    return HttpResponseRedirect('/profile/' + request.user.nickname)


def sector_war(request, sector_name):
    no_war_at_week = False

    today = datetime.date.today()
    if today.weekday() == 6:
        sun = today + datetime.timedelta(7)
    else:
        sun = today + datetime.timedelta((6 - today.weekday()) % 7)
    sat = today + datetime.timedelta((5 - today.weekday()) % 7)

    print(sat)
    print(sun)
    webhook = DiscordWebhook(url=bot_settings.SECTOR_WAR_URL)


    sector = SquadSectors.objects.get(name=sector_name)
    print(sector)
    owner = sector.squad

    enemy = Squad.objects.get(leader=request.user)
    all_wars = SectorWars.objects.all()
    for war in all_wars:
        if war.enemy == enemy or war.sector.squad == owner:
            no_war_at_week = True

    if no_war_at_week:
        messages.add_message(request, messages.WARNING, 'На этой неделе твой отряд уже участвует в боевых действиях')

    else:
        print(all_wars)
        if all_wars.count() == 2:
            print('даты заняты')
            messages.add_message(request, messages.WARNING, 'На этой неделе все даты зяняты!')
        elif all_wars.count() == 0:
            new_war = SectorWars.objects.create(sector_id=sector.id,
                                                enemy_id=enemy.id,
                                                war_date=sat,
                                                for_bot_enemy_squad_name=enemy.name,
                                                for_bot_owner_name=owner.name,
                                                for_bot_sector_name=sector.name,
                                                for_bot_owner_discord_id=owner.leader.discord_id)
            sector.in_war = True
            sector.save(force_update=True)
            new_war.save()
            new_message = PrivateMessages.objects.create(to_player_id=sector.squad.leader.id,
                                                         from_player_name=enemy.leader.personaname,
                                                         from_player_name_slug=enemy.leader.nickname,
                                                         from_player_avatar=str(enemy.leader.avatar),
                                                         text='Наш отряд притендует на сектор {} . '
                                                              'По обоюдной договоренности бой состоится {} '
                                                              'в любое время с 17 до 22 МСК. '
                                                              'В случае отказа от боя, сектор переходит под наш контроль '
                                                              'автоматически. ;)'.format(sector.name, sat.strftime('%d-%m-%Y')))
            new_message.save()


            # create embed object for webhook
            embed = DiscordEmbed(title='ОСПАРИВАНИЯ СЕКТОРА : ' + sector_name, description='Дата : ' + sat.strftime('%d-%m-%Y'), color=242424)
            embed.add_embed_field(name='Нападающие', value=enemy.name)
            embed.add_embed_field(name='Обороняющиеся', value=sector.squad.name)

            # add embed object to webhook
            webhook.add_embed(embed)

            webhook.execute()
        elif all_wars.count() == 1:
            new_war = SectorWars.objects.create(sector_id=sector.id,
                                                enemy_id=enemy.id,
                                                war_date=sun,
                                                for_bot_enemy_squad_name=enemy.name,
                                                for_bot_owner_name=owner.name,
                                                for_bot_sector_name=sector.name,
                                                for_bot_owner_discord_id=owner.leader.discord_id)
            new_war.save()
            sector.in_war = True
            sector.save(force_update=True)
            new_message = PrivateMessages.objects.create(to_player_id=sector.squad.leader.id,
                                                         from_player_name=enemy.leader.personaname,
                                                         from_player_name_slug=enemy.leader.nickname,
                                                         from_player_avatar=str(enemy.leader.avatar),
                                                         text='Наш отряд притендует на сектор {} . '
                                                              'По обоюдной договоренности бой состоится {} '
                                                              'в любое время с 17 до 22 МСК. '
                                                              'В случае отказа от боя, сектор переходит под наш контроль '
                                                              'автоматически. ;)'.format(sector.name,
                                                                                         sun.strftime('%d-%m-%Y')))
            new_message.save()
            embed = DiscordEmbed(title='ОСПАРИВАНИЯ СЕКТОРА : ' + sector_name,
                                 description='Дата : ' + sun.strftime('%d-%m-%Y'), color=242424)
            embed.add_embed_field(name='Нападающие', value=enemy.name)
            embed.add_embed_field(name='Обороняющиеся', value=sector.squad.name)

            # add embed object to webhook
            webhook.add_embed(embed)

            webhook.execute()

    return HttpResponseRedirect('/squad/#sectors_map')


def stat(request):
    if request.method == 'POST' and request.FILES:
        kills_file = request.FILES['kills_file']
        deaths_file = request.FILES['deaths_file']
        fs = FileSystemStorage()

        filename = fs.save(kills_file.name, kills_file)
        uploaded_kills_file_url = fs.url(filename)

        filename = fs.save(deaths_file.name, deaths_file)
        uploaded_deaths_file_url = fs.url(filename)

        # print(os.path.join(settings.BASE_DIR,uploaded_kills_file_url[1:]))

        with open(os.path.join(settings.BASE_DIR,uploaded_kills_file_url[1:])) as csvfile:
            reader = csv.DictReader(csvfile)
            k=0
            for row in reader:
                k +=1
                r = row['steamid;kills'].split(';')
                try:
                    u = SteamUser.objects.get(steamid=r[0])
                    u.kills += int(r[1])
                    u.save(force_update=True)
                except:
                    pass
        with open(os.path.join(settings.BASE_DIR, uploaded_deaths_file_url[1:])) as csvfile:
            reader = csv.DictReader(csvfile)
            d = 0
            for row in reader:
                d += 1
                r = row['steamid;deaths'].split(';')
                try:
                    u = SteamUser.objects.get(steamid=r[0])
                    u.deaths += int(r[1])
                    u.save(force_update=True)
                except:
                    pass


        fs.delete(os.path.join(settings.BASE_DIR,uploaded_kills_file_url[1:]))
        fs.delete(os.path.join(settings.BASE_DIR, uploaded_deaths_file_url[1:]))

        return render(request, 'squads/stat.html', locals())
    return render(request, 'squads/stat.html', locals())

def leave_squad(request):
    squad_member = SquadMembers.objects.get(player_id=request.user.id)
    new_message = PrivateMessages.objects.create(to_player_id=squad_member.squad.leader.id,
                                                     from_player_name=request.user.personaname,
                                                     from_player_name_slug=request.user.nickname,
                                                     from_player_avatar=str(request.user.avatar),
                                                     text='Я покинул отряд.')
    new_message.save()
    squad_member.delete()
    return HttpResponseRedirect('/profile/' + request.user.nickname)


def accept_war(request, sector_name):
    pass


def deny_war(request, sector_name):
    pass
