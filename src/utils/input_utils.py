################################# responsible for checking user input and reading files #################################

import os
import json
import time
import sys 

def affichage_lettre_par_lettre(texte,speed=0.05,end='\n'):
    for letter in texte:
        print(letter, end='', flush=True) #Flush in coding refers to emptying the data buffer to ensure immediate output. flush=True in print( ) forces the buffer to clear immediately
        time.sleep(speed)
    print(end)

def affichage_lettre_par_lettre_avec_input(texte,speed=0.01):
    for lettre in texte:
        print(lettre,end='',flush=True)
        time.sleep(speed)
    user_input = input()

    return user_input

def changer_statut_fichier_sauvegarde(file_path,nom_fonction):  #
    
    try : 
        with open(file_path,'r',encoding='utf-8'):
            content= json.load(file_path)

        content[nom_fonction] = True

        with open(file_path,'w',encoding='utf-8'): # represents characters in one-, two-, three-, or four-byte units. Python uses UTF-8 by default
            json.dump(content,file_path,ensure_ascii=False,indent=4)
    except FileNotFoundError:
        return('Error : file not found')

def wait_for_enter():
    """
    Attend la touche Enter sans afficher ce que tape l'utilisateur.
    Compatible Windows / Linux / macOS.
    """

    if os.name == "nt":  
        # -----------------------
        #   WINDOWS VERSION
        # -----------------------
        import msvcrt
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getwch()
                if key == '\r':  
                    print()
                    return

    else:
        # -----------------------
        #  UNIX (Linux / macOS)
        # -----------------------
        import termios
        import tty

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd) 
            while True:
                ch = sys.stdin.read(1)
                if ch == '\r' or ch == '\n': 
                    print()
                    return
      
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def ask_text(message:str)->str:
    """
    Ask the user for a text input with optional validation.

    Args:
        message (str): The message to display to the user.

    Returns:
        str: The input text 
    """

    text = affichage_lettre_par_lettre_avec_input(message)
 
    if  text == '' or text == ' '*len(text):
        return ask_text(f"{message}")

    res = text.strip()
    return res



def convertisseur_str_to_integer(s: str) -> int:
    s = s.strip()  
    
    negative = False
    if not s:
        raise ValueError("La chaîne est vide")
    if s[0] == '-':
        negative = True
        s = s[1:]
    elif s[0] == '+':   
        s = s[1:]
    
    
    result = 0
    for char in s:
        if not char in '1234567890':
            raise ValueError(f"'{char}' n'est pas un chiffre valide")
    
        result = result * 10 + (ord(char) - ord('0'))
    
    return -result if negative else result

 

def ask_number(message:str,min_val:int,max_val:int)->int:
    number_str = affichage_lettre_par_lettre_avec_input(message)
    
    if number_str == '' or number_str == " "*len(number_str):
        affichage_lettre_par_lettre(f'Enter an integer')
        return ask_number(message,min_val,max_val)

    try:

        number = convertisseur_str_to_integer(number_str)
    except ValueError:

        affichage_lettre_par_lettre(f"Please enter a integer")
        return ask_number(message,min_val,max_val)


    if min_val is None and max_val is None:

        return number

    elif min_val is None:

        if number > max_val:

            affichage_lettre_par_lettre(f"Please enter a number lower than {max_val}.")
            return ask_number(message,min_val,max_val)

        return number

    elif max_val is None:
        if number < min_val:
            affichage_lettre_par_lettre(f"Please enter a number greater than {min_val}.")
            return ask_number(message,min_val,max_val)
        return number

    else:
        if number < min_val or number > max_val:
            affichage_lettre_par_lettre(f"Please enter a number between {min_val} and {max_val}.")
            return ask_number(message,min_val,max_val)
        return number


def ask_choice(message: str, options: list) -> str:

    affichage_lettre_par_lettre(message)

    for i in range(len(options)):
        affichage_lettre_par_lettre(f"{i+1}. {options[i]}")

    choice_str = affichage_lettre_par_lettre_avec_input("Your choice: ")

    try:
        choice = convertisseur_str_to_integer(choice_str)
    except ValueError:
        affichage_lettre_par_lettre(f"Please enter the number and not the text")
        return ask_choice(message, options)

    if choice < 1 or choice > len(options):
        affichage_lettre_par_lettre(f"Please enter a choice between 1 and {len(options)}")
        return ask_choice(message, options)

    return choice - 1 # type: ignore


def load_file(file_path:str)->dict:
    if not os.path.isfile(file_path): 
        return {"error": "Chemin n'existe pas"}

    with open(file_path,'r', encoding='utf-8') as f1:
        return json.load(f1)
    
def bold(text):
    return f"\033[1m{text}\033[0m"

def charger_personnage(file_path= "src/chapters/sauvegardes/sauvegarde_donnees_personnage.json"):

    from src.universe.character import Character
    from src.universe.house import House

    content= load_file(file_path) 

    last_name = content['Last name']
    first_name = content['First name']
    attributes = {
        'courage': int(content['Courage level']),
        'intelligence' : int(content['Intelligence level']),
        'loyalty' : int(content['Loyalty level']),
        'ambition' : int(content['Ambition level'])
                  }
    money = int(content['Money'])
    inventory = content['Inventory']
    spells = content['Spells']
    house = content['House']

    return Character(last_name,first_name,attributes,money,inventory,spells,House(house))
