#Guided scenario: Quidditch match



from src.universe.character import Character
from src.universe.house import House


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