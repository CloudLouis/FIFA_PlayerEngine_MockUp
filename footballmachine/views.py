from django.http import HttpResponse
from django.template import loader
from .models import Players
import footballmachine.teamcalculator as tc

def index(request):
    template = loader.get_template('footballmachine/index.html')
    context = {'temp' : "temp"}
    return HttpResponse(template.render(context, request))
    """
    players = Players.objects.all()[:10]
    template = loader.get_template('footballmachine/index.html')
    context = {
        'player_list' : players,
    }
    return HttpResponse(template.render(context, request))
    """

def search_result(request):
    criteria = request.POST.get('criteria')
    query = '%%'+request.POST.get('query')+'%%'
    sqlQuery = "SELECT * FROM footballmachine_players WHERE "+criteria+" LIKE '"+query+"'"
    player_list = Players.objects.raw(sqlQuery)
    template = loader.get_template('footballmachine/search_result.html')
    context = {'player_list' : player_list}
    return HttpResponse(template.render(context,request))

def builder_result(request):
    budget = request.GET.get('budget')
    team, total_player_value = tc.calculate_team(budget)
    template = loader.get_template('footballmachine/builder_result.html')
    context = {
        'team' : team,
        'budget' :budget,
        'total_player_value': total_player_value,
        }
    return HttpResponse(template.render(context,request))


