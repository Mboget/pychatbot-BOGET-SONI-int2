################################## Chapter 1 ##################################

from src.utils.input_utils import affichage_lettre_par_lettre
from src.utils.input_utils import affichage_lettre_par_lettre_avec_input
from src.utils.input_utils import ask_text
from src.utils.input_utils import ask_choice
from src.utils.input_utils import ask_number
from src.utils.input_utils import load_file
from src.utils.input_utils import bold
from src.utils.input_utils import wait_for_enter
from src.universe.character import Character
from src.universe.house import House
from src.utils.input_utils import changer_statut_fichier_sauvegarde
import os
import json

def introduction():

    changer_statut_fichier_sauvegarde("src/chapters/chapter_1",'introduction')

    text = """
    Something strange lingers in the air today
    You can't quite explain it, but you feel it.
    As if a secret has been waiting for you all along.

    You are still just an ordinary child living an ordinary life 
    but this morning, everything is about to change.
    A sudden thump echoes against the window
    and a dark shape glides across the sky.

    Before you can react, a letter, sealed with an elegant crest shaped like an interlaced H, lands at your feet.

    Your heart quickens as you pick it up:
    What if your suspicions were true?
    What if magic was real?

    You're about to discover a world you never knew existed 
    a world of spells, mysteries, and unforgettable adventures.

    Your journey begins now.
    Welcome to the Wizarding World.

    """
    affichage_lettre_par_lettre(text)
    affichage_lettre_par_lettre("Press Enter to begin your adventure...")
    wait_for_enter()

def create_character()->Character:
    """
    Create a character and assign attributes to it.

    This function asks the user to input the character's last name, first name, and four attributes: courage, intelligence, loyalty, and ambition.
    It then creates a Character object with these attributes and displays the character's profile.
    """

    changer_statut_fichier_sauvegarde("src/chapters/chapter_1",'create_character')

    last_name = ask_text("Enter your character's last name: ")

    first_name = ask_text("Enter your character's first name: ")

    affichage_lettre_par_lettre("Choose your attributes: ")

    courage_level = ask_number("Courage level (1-10): ",1,10)
    intelligence_level = ask_number("Intelligence level (1-10): ",1,10)
    loyalty_level = ask_number("Loyalty level (1-10): ",1,10)
    ambition_level = ask_number("Ambition level (1-10): ",1,10)

    mes_attribues = {
        "courage": courage_level,
        "intelligence": intelligence_level,
        "loyalty": loyalty_level,
        "ambition": ambition_level
    }

    personnage = Character(last_name, first_name, mes_attribues)

    personnage.display_character()

    if not os.path.isfile("src/chapters/sauvegardes/sauvegarde_donnees_personnage.json"): 
        data = {
            "Last name" : personnage.last_name ,
            "First name" : personnage.first_name,
            "Money" : personnage.money,
            "Attributes" : personnage.attributes,
            "Inventory" : personnage.inventory,
            "Spells" : personnage.spells,
            "House" : personnage.house,
        }

        with open("src/chapters/sauvegardes/sauvegarde_donnees_personnage.json","w",encoding="utf-8") as j1:
            json.dump(data,j1,ensure_ascii=False,indent=4)

    return personnage

def receive_letter(character: Character):
    changer_statut_fichier_sauvegarde("src/chapters/chapter_1",'receive_letter')

    text = f"""
    An owl flies through the window, delivering a letter sealed with the Hogwarts crest...
    
    "Dear {character.last_name} {(character.first_name)}, 
    We are pleased to inform you that you have been accepted to Hogwats School of Witchcraft and Wizardry!"

    """
    affichage_lettre_par_lettre(text)

    choice_accept_hogwarts = ask_choice("Do you accept this invitation and go to Hogwarts?",["Yes, of course!","No, I'd rather stay with Uncle Vernon..."])
    
    if choice_accept_hogwarts == 1:

        texte = """
    Your tear up the letter, and Uncle Vernon cheers:

    "EXCELLENT! Finally someone NORMAL in this house!"

    The magical world will never know you existed... 

    The uncle vernon in your universe is cool??? 
    Game over you fool. 
                """
        affichage_lettre_par_lettre(texte)
        exit()

def meet_hagrid(character:Character):

    changer_statut_fichier_sauvegarde("src/chapters/chapter_1",'meet_hagrid')

    texte = f"""
    Hagrid : "Hello {character.first_name}! I'm here to help you with your shopping on Diagon Alley."
             """
    affichage_lettre_par_lettre(texte)

    choice_follow_hagrid = ask_choice("Do you want to follow Hagrid?",["Yes","No"])

    if choice_follow_hagrid == 1:
        texte = """
        Hagrid gently insists and takes you along anyway! 
        (You think that you can play smart with me ???)
                    """
        affichage_lettre_par_lettre(texte)


def buy_supplies(character:Character):
    """
    This function simulates the process of buying school supplies for Hogwarts.
    It takes a Character object as an argument and modifies its attributes accordingly.
    """
    
    changer_statut_fichier_sauvegarde("src/chapters/chapter_1",'buy_supplies')

    contenu_diagon_alley =load_file("src/data/inventory.json")
    required_items = []

    affichage_lettre_par_lettre(bold("Welcome to Diagon Alley !"))
    
    affichage_lettre_par_lettre("Catalog of available items :")
    for key,val in contenu_diagon_alley.items():
        
        if val[2] == "required":
            affichage_lettre_par_lettre(f'{key}. {val[0]} - {val[1]} Galleons (required)')
            required_items.append(val[0])

        else: 
            affichage_lettre_par_lettre(f'{key}. {val[0]} - {val[1]} Galleons (optional)')
    
    item_bought = []

    while required_items and character.money > 0:
        affichage_lettre_par_lettre(f"You have {character.money} Galleons.")
        affichage_lettre_par_lettre("Remaining required items:")

        list_required = [(key, val) for key, val in contenu_diagon_alley.items() if val[2] == "required" and val[0] in required_items]

        if not list_required:
            break

        affordable = [entry for entry in list_required if entry[1][1] <= character.money]
        if not affordable:
            break

        options = [f"{val[0]} - {val[1]} Galleons" for _, val in affordable]
        choice_idx = ask_choice("Which required item do you want to buy?", options)

        selected_key, selected_val = affordable[choice_idx] # type: ignore
        price = selected_val[1]

        character.money -= price
        item_bought.append(selected_val[0])
        if selected_val[0] in required_items:
            required_items.remove(selected_val[0])

    if required_items != []: 
        texte = """
    You don't know how to manage a 100 Galleons budget.
    I wonder what your bank account looks like...
    Game over !
                """
        affichage_lettre_par_lettre(texte)
        exit()

    affichage_lettre_par_lettre("It's time to choose your Hogwats pet!")

    if character.money < 5:
        texte = f"""
    You have {character.money} Galleons good luck to buy a pet for that, we aren't charity you idiot !
    Game Over
        """
        affichage_lettre_par_lettre(texte)
        exit()

    texte = f"""
    You have {character.money} Galleons. 
        """
    affichage_lettre_par_lettre(texte)

    pets =load_file("src/data/pets.json")
    liste_pets = []

    affichage_lettre_par_lettre("Catalog of available pets :")
    
    for key,val in pets.items():
        affichage_lettre_par_lettre(f'{key}. {val[0]} - {val[1]} Galleons (optional)')
        liste_pets.append(val[0])

    attempt_choice_pet = ask_choice("Which pet do you want?",liste_pets)

    while pets[str(attempt_choice_pet+1)][1]> character.money: # type: ignore
        affichage_lettre_par_lettre("Remember you're broke brother... \nChoose an other pet.")
        attempt_choice_pet = ask_choice("Which pet do you want?",liste_pets)

    affichage_lettre_par_lettre(f"You chose : {pets[str(attempt_choice_pet+1)][0]} (-{pets[str(attempt_choice_pet+1)][1]} Galleons).") # type: ignore
    item_bought.append(pets[str(attempt_choice_pet+1)][0]) #type: ignore

    affichage_lettre_par_lettre("Every thing you need to succed have been successfully purchased ! Here is your final inventory :")
    character.add_item('inventory',item_bought)
    character.display_character()

    

def start_chapter_1():
    if not os.path.isfile("src/chapters/sauvegardes/sauvegarde_chapter_1.json"): 
        data = {
            "1" : {"introduction": False}, # type: ignore
            "2" : {"create_character": False}, # type: ignore
            "3" : {"receive_letter": False}, # type: ignore
            "4" : {"meet_hagrid": False}, # type: ignore
            "5" : {"buy_supplies": False} # type: ignore
        }

        with open("src/chapters/sauvegardes/sauvegarde_chapter_1.json","w",encoding="utf-8") as j1:
            json.dump(data,j1,ensure_ascii=False,indent=4)

    with open("src/chapters/sauvegardes/sauvegarde_chapter_1.json",'r',encoding="utf-8") as f1:
        content = json.load(f1)

    chaptire_en_cours = None 
    trouve = False 

    for key,val in content.items():
        for key2,val2 in val.items():
            if val2 == False and not trouve:  # type: ignore
                chaptire_en_cours = key2
                trouve = True

    match chaptire_en_cours:
        case "intro":
            introduction()
            perso_joueur = create_character()
            receive_letter(perso_joueur)
            meet_hagrid(perso_joueur)
            buy_supplies(perso_joueur)

        case "creation_character":
            perso_joueur = create_character()
            receive_letter(perso_joueur)
            meet_hagrid(perso_joueur)
            buy_supplies(perso_joueur)

        case "receiving letter":
            if not os.path.isfile("src/chapters/sauvegardes/sauvegarde_donnees_personnage.json"): 
                perso_joueur = create_character()
            else : 
                with open("src/chapters/sauvegardes/sauvegarde_donnees_personnage.json","r",encoding="utf-8") as j1:
                    donnees_personnage = json.load(j1)
                
                last_name = donnees_personnage["Last name"]
                first_name = donnees_personnage["First name"]
                mes_attribues = donnees_personnage["Attributes"]
                money = donnees_personnage["Money"]
                inventory = donnees_personnage["Inventory"]
                spells = donnees_personnage["Spells"]
                house = donnees_personnage["House"]

                perso_joueur = Character(last_name,first_name,mes_attribues,money,inventory,spells,House(house))

            receive_letter(perso_joueur)
            meet_hagrid(perso_joueur)
            buy_supplies(perso_joueur)




if __name__ == "__main__":
    start_chapter_1()