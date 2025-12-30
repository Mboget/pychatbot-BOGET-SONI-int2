#Guided scenario: Quidditch match
import random

from src.universe.character import Character
from src.universe.house import House
from src.utils.input_utils import affichage_lettre_par_lettre


def create_team(house_name, team_data, is_player=False, player=None):
    """
    Creates a team dictionary from the JSON data.
    If it is the player's team, replaces the Seeker with the player's name.
    """
    # Create a copy of the players list to avoid modifying the original loaded data
    players_list = team_data["players"].copy()

    # If this is the player's team, replace the default Seeker (Index 0)
    if is_player and player:
        # Construct player's display name
        player_display_name = f"{player.first_name} {player.last_name} (Seeker)"
        players_list[0] = player_display_name

    # Initialize the team dictionary structure
    team = {
        "name": house_name,
        "score": 0,
        "goals_scored": 0,
        "goals_blocked": 0,
        "caught_snitch": False,
        "players": players_list,
        "captain": team_data["captain"]
    }

    return team

def attempt_goal(attacking_team, defending_team, player_is_seeker=False):
    chance_goal= random.randint(1,10)
    players_list = attacking_team["players"]

    if chance_goal >= 6:
        if player_is_seeker==True:
            scorer= players_list[0]
        else:
            which_player= random.randint(1,len(players_list)-1)
            scorer= players_list[which_player]

        attacking_team["score"] += 10
        attacking_team["goals_scored"] += 1
        affichage_lettre_par_lettre("{} scores a goal for {}! (+10 points)".format(scorer, attacking_team["name"]))
    else:
        defending_team["goals_blocked"] += 1
        affichage_lettre_par_lettre("{} blocks the attack!".format(defending_team["name"]))

def golden_snitch_appears():
    return random.randint(1, 6) == 6


def catch_golden_snitch(e1, e2):
    #e1 & e2 are dictionarries
    winner = random.choice([e1, e2])
    winner['score'] += 150
    winner['caught_snitch'] = True

    # Narrate the catch (Seeker is index 0)
    seeker_name = winner['players'][0]
    affichage_lettre_par_lettre(bold(f"\n✨ THE GOLDEN SNITCH HAS BEEN CAUGHT! ✨"))
    affichage_lettre_par_lettre(f"{seeker_name} dives and catches it for {winner['name']}!")
    affichage_lettre_par_lettre(f"{winner['name']} gains 150 points!")
    return winner

def display_score(e1, e2):
    affichage_lettre_par_lettre("/nCurrent score")
    affichage_lettre_par_lettre(f"-> {e1['name']} : {e1['score']}points")
    affichage_lettre_par_lettre(f"-> {e2['name']} : {e2['score']}points")

def display_team(house, team):
    affichage_lettre_par_lettre(f"{house} team:")
    for player in team['players']:
        affichage_lettre_par_lettre(f"- {player}")



