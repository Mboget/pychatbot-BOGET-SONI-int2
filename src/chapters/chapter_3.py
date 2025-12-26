################################## Chapter 3 ##################################

from src.utils.input_utils import affichage_lettre_par_lettre
from src.utils.input_utils import affichage_lettre_par_lettre_avec_input
from src.utils.input_utils import load_file
from src.utils.input_utils import wait_for_enter
from src.universe.character import Character
from src.utils.input_utils import charger_personnage
from src.utils.input_utils import changer_statut_fichier_sauvegarde
from src.universe.house import display_winning_houses, House
from random import randint, sample
import json 
import os

def learn_spells(character, file_path="src/data/spells.json"):

    changer_statut_fichier_sauvegarde("src/chapters/chapter_3",'learn_spells')

    content = load_file(file_path)

    offensive_spells = []
    defensive_spells = []
    utility_spells = []

    for spell in content:   
 
        if spell["type"] == "Utility":
            utility_spells.append(spell)
        if spell["type"] == "Defensive":
            defensive_spells.append(spell)
        if spell["type"] == "Offensive":
            offensive_spells.append(spell)

    random_offensive_spell = [offensive_spells[randint(0,len(offensive_spells)-1)]]
    random_defensive_spell = [defensive_spells[randint(0,len(defensive_spells)-1)]]
    random_utility_spell = [utility_spells[randint(0,len(utility_spells)-1)] for _ in range(3)]


    spell_learned = random_defensive_spell + random_offensive_spell + random_utility_spell
    spell_learned = sample(spell_learned,len(spell_learned))

    affichage_lettre_par_lettre("You begin your magic session at Hogwarts... ")

    for spell in spell_learned:
        texte = f"You have just learned the spell: {spell['name']}, ({spell['type']})"
        affichage_lettre_par_lettre(texte)
        texte = "Press enter to continue..."
        affichage_lettre_par_lettre(texte)
        wait_for_enter()

    texte = """
    You have completed your basic spell training at Hogwarts!
    Here are the spells you now master:
    """

    for spell in spell_learned:
        texte = f"- {spell['name']} ({spell['type']}): {spell['description']}"
        affichage_lettre_par_lettre(texte)

def magic_quiz(character:Character,file_path = 'src/data/quiz_magie.json'): 

    changer_statut_fichier_sauvegarde("src/chapters/chapter_3",'magic_quiz')

    texte = """
    Welcome to the Hogwats Quizz !
    Answer the 4 questions correctly to earn points for your house. 
    """
    affichage_lettre_par_lettre(texte)

    with open(file_path,'r', encoding='utf-8') as quiz:
        content = json.load(quiz)

    quiz_items = []
    for item in content:
        q = item.get('question')
        a = item.get('answer')
        if q is not None and a is not None:
            quiz_items.append((q, a))

    nb = min(4, len(quiz_items))
    question_reponse_quiz = sample(quiz_items, nb)

    for question, reponse in question_reponse_quiz:
        texte = question
        reponse_user = affichage_lettre_par_lettre_avec_input(texte)

        if reponse_user and reponse_user.strip().lower() == str(reponse).strip().lower():
            character.house.ajout_point(25)
            texte = f"Correct answer, +25 points for {character.house.nom}"
            affichage_lettre_par_lettre(texte)
        else:
            texte = f"Wrong answer. The correct answer was: {reponse}"
            affichage_lettre_par_lettre(texte)

def start_chapter_3(perso:Character):
    if not os.path.isfile("src/chapters/sauvegardes/sauvegarde_chapter_3.json"): 
        data = {
            "1" : {"learn_spells": False}, # type: ignore
            "2" : {"magic_quiz": False}, # type: ignore
        }

        with open("src/chapters/sauvegardes/sauvegarde_chapter_3.json","w",encoding="utf-8") as j1:
            json.dump(data,j1,ensure_ascii=False,indent=4)

    with open("src/chapters/sauvegardes/sauvegarde_chapter_3.json",'r',encoding="utf-8") as f1:
        content = json.load(f1)

    chaptire_en_cours = None 
    trouve = False 

    for key,val in content.items():
        for key2,val2 in val.items():
            if val2 == False and not trouve:  # type: ignore
                chaptire_en_cours = key2
                trouve = True

    if perso == {"error": "Chemin n'existe pas"}:
        affichage_lettre_par_lettre("You have to do the history in the right order !")
        exit()

    match chaptire_en_cours:
        case "learn_spells":
            learn_spells(perso)
            magic_quiz(perso)
            display_winning_houses([House("Gryffindor"),House("Slytherin"),House("Hufflepuff"),House("Ravenclaw")])
            perso.display_character()
        case "magic_quiz":
            magic_quiz(perso)
            display_winning_houses([House("Gryffindor"),House("Slytherin"),House("Hufflepuff"),House("Ravenclaw")])
            perso.display_character()

if __name__ == '__main__':

    perso = charger_personnage()
    start_chapter_3(perso)

