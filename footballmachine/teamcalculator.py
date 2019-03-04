from .models import Players
from django.db.models import Q
import pandas as pd

def calculate_team(budget):
    total_player_value = 0
    goalkeepers = pd.DataFrame.from_records(Players.objects.filter(Position="GK").values("Name", "Age", "Nationality", "Club", "Photo","ID", "Position", "Value", "Overall"))
    fullbacks = pd.DataFrame.from_records(
        Players.objects.filter(Q(Position="LB") | Q(Position="RB") | Q(Position="LWB") | Q(Position="RWB")).values("Name", "Age", "Nationality", "Club", "Photo","ID", "Position", "Value", "Overall")
    )
    halfbacks = pd.DataFrame.from_records(
        Players.objects.filter(Q(Position="CB") | Q(Position="LCB") | Q(Position="RCB") | Q(Position="CDM") | Q(Position="LDM") | Q(Position="RDM") | Q(Position="CM") | Q(Position="LCM") | Q(Position="RCM") |  Q(Position="LM") | Q(Position="RM")).values("Name", "Age", "Nationality", "Club", "Photo","ID", "Position", "Value", "Overall")
    )
    forwards = pd.DataFrame.from_records(
        Players.objects.filter(Q(Position="CAM") | Q(Position="LAM") | Q(Position="RAM") | Q(Position="LWF") | Q(Position="RWF") | Q(Position="CF") | Q(Position="LCF") | Q(Position="RCF")).values("Name", "Age", "Nationality", "Club", "Photo","ID", "Position", "Value", "Overall")
    )
    team, total_player_value = initialize_team(budget, goalkeepers, fullbacks, halfbacks, forwards)
    return team, total_player_value

def on_budget(budget, team):
    status = False
    total = 0
    for p in team:
        total = total + parse_value(p['Value'])
    if total <= float(budget):
        status = True
    else:
        status = False
    return status

def parse_value(value):
    if 'K' in value :
        value = value.translate(str.maketrans(dict.fromkeys('€K')))
        value = float(value)*1000
    elif 'M' in value:
        value = value.translate(str.maketrans(dict.fromkeys('€M')))
        value = float(value)*1000000
    else:
        value = value.translate(str.maketrans(dict.fromkeys('€')))
        value = float(value)*1
    return value

def initialize_team(budget, goalkeepers, fullbacks, halfbacks, forwards):
    total_value=0
    team = []
    budget_for_one = float(budget)/11
    to_add, goalkeepers = get_player(budget_for_one, goalkeepers)
    team.append(to_add)
    total_value = total_value+parse_value(to_add['Value'])
    for i in range(2):
        to_add, fullbacks = get_player(budget_for_one, fullbacks)
        team.append(to_add)
        total_value = total_value+parse_value(to_add['Value'])
    for i in range(3):
        to_add, halfbacks = get_player(budget_for_one, halfbacks)
        team.append(to_add)
        total_value = total_value+parse_value(to_add['Value'])
    for i in range(5):
        to_add, forwards = get_player(budget_for_one, forwards)
        team.append(to_add)
        total_value = total_value+parse_value(to_add['Value'])
    return team, total_value

def get_player(limit, player_pool):
    original_pool = player_pool
    status = True
    best_player = None
    while status:
        max_overall = player_pool.loc[player_pool['Overall'].idxmax()]
        if parse_value(max_overall['Value']) <= limit:
            best_player = max_overall
            original_pool = original_pool[original_pool.ID != max_overall.ID]
            status = False
        else:
            player_pool = player_pool[player_pool.ID != max_overall.ID]
    return best_player, original_pool
