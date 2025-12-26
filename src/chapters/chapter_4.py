from src.universe.character import Character
from src.universe.house import House


def create_team(house, team_data, is_player=False, player=None): #

    team = {
        'name': house,
        'score': 0,
        'goals_scored': 0,
        'goals_blocked': 0,
        'caught_snitch': False,
        'players': []
    }

    your_team=[]
    if house in team_data:
        your_team = list(team_data[house]['players'])

    if is_player and player:
        player_str = f"{player.first_name} {player.last_name} (Seeker)"

        if len(team['players']) > 0:
            team['players'][0] = player_str
        else:
            team['players'].append(player_str)

    return team

