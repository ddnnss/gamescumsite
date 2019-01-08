from authentication.models import PrivateMessages
from squads.models import Squad,SquadMembers,SquadSectors,SectorWars
from shop.models import Orders

def check_profile(request):
    if request.user.is_authenticated:
        pm = PrivateMessages.objects.filter(to_player_id=request.user.id).order_by('-created')
        orders_count = Orders.objects.filter(player_id=request.user.id, is_complete=False).count()
        if request.user.discord_id == None:
            profile_bad = True
        else:
            profile_bad = False

    return locals()

def get_player_squad_info(request):
    if request.user.is_authenticated:
        try:
            player_squad_member = SquadMembers.objects.get(player=request.user.id)
            player_squad = player_squad_member.squad
            player_squad_sector = SquadSectors.objects.filter(squad=player_squad.id)
            if request.user.id == player_squad.leader.id:
                sector_wars = SectorWars.objects.filter(sector__in=player_squad_sector)
            print(player_squad_sector)

        except:
            player_squad_member = None

    return locals()