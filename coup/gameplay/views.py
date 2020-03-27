from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
import json

from .play import Gameplay

from .forms import PlayerForm
def index(request):
    return HttpResponse(status=200)

@csrf_exempt
def get_name(request):
    print("IN GET NAME")
    if request.method == 'POST':
        playerDict = json.loads(request.body)
        request.session['name'] = playerDict['name']
        gameplay = Gameplay()
        gameplay.addPlayer(playerDict['name'])

        return HttpResponse(json.dumps({'name': request.session['name']}), status=200,  content_type="application/json" )


def gameState(request):
    gameplay = Gameplay()
    players = gameplay.getOrder()
    myPlayer = gameplay.getPlayer(request.GET['name'])
    context = {
        'myPlayer': myPlayer,
        'players': players,
    }
    return HttpResponse(json.dumps(context), status=200, content_type="application/json")