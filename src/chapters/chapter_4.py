#Guided scenario: Quidditch match
import random

from src.universe.character import Character
from src.universe.house import House

from src.utils.input_utils import affichage_lettre_par_lettre
from src.utils.input_utils import affichage_lettre_par_lettre_avec_input
from src.utils.input_utils import load_file
from src.utils.input_utils import wait_for_enter
from src.utils.input_utils import bold
from src.utils.input_utils import charger_personnage
from src.utils.input_utils import changer_statut_fichier_sauvegarde
from src.universe.house import display_winning_houses, House
from random import randint, sample
import json
import os


def create_team(house_name, team_data, is_player=False, player=None):

    players_list = team_data["players"][:]

    if is_player and player:
        player_display_name = f"{player.first_name} {player.last_name} (Seeker)"
        players_list[0] = player_display_name

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
    winner = random.choice([e1, e2])
    winner['score'] += 150
    winner['caught_snitch'] = True

    seeker_name = winner['players'][0]
    affichage_lettre_par_lettre(bold(f"✨ THE GOLDEN SNITCH HAS BEEN CAUGHT! ✨"))
    affichage_lettre_par_lettre(f"{seeker_name} dives and catches it for {winner['name']}!")
    affichage_lettre_par_lettre(f"{winner['name']} gains 150 points!")
    return winner

def display_score(e1, e2):
    affichage_lettre_par_lettre("Current score")
    affichage_lettre_par_lettre(f"-> {e1['name']} : {e1['score']}points")
    affichage_lettre_par_lettre(f"-> {e2['name']} : {e2['score']}points")

def display_team(house, team):
    affichage_lettre_par_lettre(f"{house} team:")
    for player in team['players']:
        affichage_lettre_par_lettre(f"- {player}")



def quidditch_match(character, houses):
    teams_data = load_file("src/data/equipes_quidditch.json")

    player_house_name = character.house.nom

    possible_opponents = []

    for name in teams_data.keys():
        
        if name != player_house_name:
            possible_opponents.append(name)

    opponent_house_name = random.choice(possible_opponents)
    affichage_lettre_par_lettre(f"Quidditch Match: {player_house_name} vs {opponent_house_name}!")

    my_team=create_team(player_house_name, teams_data[player_house_name], is_player=True, player=character)
    opp_team = create_team(opponent_house_name, teams_data[opponent_house_name], is_player=False)

    display_team(player_house_name, my_team)
    affichage_lettre_par_lettre(f"Press enter to continue")
    wait_for_enter()

    print()
    display_team(opponent_house_name, opp_team)

    affichage_lettre_par_lettre(f"you are playing for {player_house_name} as a seeker")
    match_ended_by_snitch = False
    for turn in range(5,21):
        affichage_lettre_par_lettre(f"----- turn {turn - 4}-----")
        attempt_goal(my_team, opp_team, player_is_seeker=True)
        attempt_goal(opp_team, my_team, player_is_seeker=False)

        display_score(my_team, opp_team)

        if golden_snitch_appears():
            winner_snitch = catch_golden_snitch(my_team, opp_team)
            affichage_lettre_par_lettre(f"The Golden Snitch has been caught by {winner_snitch['name']}! (+150 points)")
            match_ended_by_snitch = True
            winning_team_name = winner_snitch['name']
            wait_for_enter()
            break

        affichage_lettre_par_lettre(f"Press enter to continue")
        wait_for_enter()

    # Fin du match (après toutes les manches ou si la snitch a été attrapée)
    affichage_lettre_par_lettre("End of match!")
    display_score(my_team, opp_team)

    winning_team_name = ""
    if my_team['score'] > opp_team['score']:
        winning_team_name = my_team['name']
        affichage_lettre_par_lettre(f"{winning_team_name} wins!!!")
    elif my_team['score'] < opp_team['score']:
        winning_team_name = opp_team['name']
        affichage_lettre_par_lettre(f"{winning_team_name} wins!!!")
    else:
        affichage_lettre_par_lettre("It's a TIE !!!!")

    if winning_team_name:
        affichage_lettre_par_lettre(f" +500 points to {winning_team_name}!")
        for house_obj in houses:
            if house_obj.nom == winning_team_name:
                house_obj.ajout_point(500)
                affichage_lettre_par_lettre(f"Total: {house_obj.nombre_point} points.")



def start_chapter_4(character,houses):

    affichage_lettre_par_lettre("CHAPTER 4: THE GOLDEN SNITCH")
    affichage_lettre_par_lettre("-" * 50)
    text = """
The year is coming towards an end 
however let's finish it off with the anticipated quiditch match!!!
The atmosphere is cheerful.
Flags are waving and the students are chanting their house names.
You grip your broomstick tightly thrilled to be on the team"""

    affichage_lettre_par_lettre(text)
    affichage_lettre_par_lettre(f"Press enter to continue")
    wait_for_enter()

    quidditch_match(character,houses)

    affichage_lettre_par_lettre("\n" + "-" * 50)
    affichage_lettre_par_lettre("End of Chapter 4 — What an incredible performance on the field!")
    affichage_lettre_par_lettre("-" * 50)
    wait_for_enter()

    wining_house_name = display_winning_houses(houses)
    affichage_lettre_par_lettre(f"\n And the winner is... {wining_house_name} ! 🏆")
    affichage_lettre_par_lettre("Here is your final wizard profile:")

    character.display_character()

    affichage_lettre_par_lettre("Thank you for playing Hogwarts!")


if __name__ == "__main__":
    perso = charger_personnage()

    houses = houses = [House("Gryffindor"),House("Slytherin"),House("Hufflepuff"),House("Ravenclaw")]
    start_chapter_4(perso,houses)

