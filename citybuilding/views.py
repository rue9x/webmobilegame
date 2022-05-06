from django.shortcuts import render
from django.contrib.auth.models import User, auth
from accounts.models import PlayerData
import json
def home(request): 
    
    # area_unlock, barracks, current_hero, iap_cash, id, plots, renown, user, user_id
    data = PlayerData.objects.get(pk=request.user.playerdata.pk)
    pd = {
        "area_unlock" : int(data.area_unlock),
        "barracks" : dict(data.barracks),
        "current_hero" : int(data.current_hero),
        "iap_cash" : round(float(data.iap_cash),3),
        "id" : int(data.id),
        "plots" : dict(data.plots),
        "renown" : int(data.renown),
        "user" : str(data.user),
        "user_id" : data.user_id
    
    }
    return render(request, 'cityscreen.html',{"data": json.dumps(json.dumps(pd))})

