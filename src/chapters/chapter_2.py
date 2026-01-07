
from src.universe.character import Character

from src.utils.input_utils import load_file,ask_choice,affichage_lettre_par_lettre,charger_personnage

def meet_friends(character):
    print()
    affichage_lettre_par_lettre("you board the train which is slowly departing northward...")

    affichage_lettre_par_lettre("\n A red-haired boy enters your compartment, looking friendly.")
    
    choice = ask_choice("how do you respond?",["Sure have a seat","Sorry I prefer to travel alone."])

    if choice == 0:
        character.attributes['loyalty'] +=1
        affichage_lettre_par_lettre("Ron smiles: Awesome! You'll see, Hogwarts is amazing!")

    else:
        character.attributes['ambition'] += 1
        affichage_lettre_par_lettre("Ron shrugs and moves on")

    affichage_lettre_par_lettre("A girl enters next, already carrying a stack of books.")
    affichage_lettre_par_lettre("— Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?")
    choice = ask_choice("How do you respond?", ["Yes, I love learning new things!","Uh... no, I prefer adventures over books."])

    if choice == 0:
        affichage_lettre_par_lettre("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!")
        character.attributes['intelligence'] +=1
    else:
        affichage_lettre_par_lettre("Hermione looks disappointed and leaves")
        character.attributes['courage'] += 1

    affichage_lettre_par_lettre("Then a blonde boy enters, looking arrogant.")
    affichage_lettre_par_lettre("I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?")
    choice = ask_choice("How do you respond?", ["Shake his hand politely.", "Ignore him completely.", "Respond with arrogance."])
    
    if choice == 0:
        affichage_lettre_par_lettre("You are a good judge of character")
        character.attributes['ambition'] += 1
    elif choice == 1:
        affichage_lettre_par_lettre("HOW DARE YOU IGNORE ME ! Father will be hearing about this")
        character.attributes['loyalty'] +=1
    else:
        character.attributes['courage'] += 1
        affichage_lettre_par_lettre("You will regret this!")


    affichage_lettre_par_lettre("Your updated attributes are:")
    for attr, value in character.attributes.items():
        affichage_lettre_par_lettre(f" - {attr}: {value}")


def sorting(character):
    questions = [
        (
            "You see a friend in danger. What do you do?",
            ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"],
             ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "Which trait describes you best?",
            ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"],
             ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "When faced with a difficult challenge, you...",
            ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends","Analyze the problem"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        )
    ]
    affichage_lettre_par_lettre("The sorting ceremony begins in the Great Hall...")
    affichage_lettre_par_lettre("The Sorting Hat observes you for a long time before asking its questions:")


    house_scores = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    attributes = character.attributes

    house_scores["Gryffindor"] += attributes.get('courage', 0) * 2
    house_scores["Slytherin"] += attributes.get('ambition', 0) * 2
    house_scores["Hufflepuff"] += attributes.get('loyalty', 0) * 2
    house_scores["Ravenclaw"] += attributes.get('intelligence', 0) * 2

    for question_text, options, house_assignments in questions:

        chosen_index = ask_choice(question_text, options)
        assigned_house = house_assignments[chosen_index] # type: ignore
        house_scores[assigned_house] += 3

    affichage_lettre_par_lettre("Summary of scores:")
    for house, score in house_scores.items():
        affichage_lettre_par_lettre(f"{house}: {score} points")

    max_score = max(house_scores.values())
    winning_houses = [house for house, score in house_scores.items() if score == max_score]
    final_house_name = winning_houses[0]
    character.house.nom = final_house_name
    affichage_lettre_par_lettre(f"The Sorting Hat exclaims: **{final_house_name.upper()}!!!**")
    affichage_lettre_par_lettre(f"You join the {final_house_name} students to loud cheers!")


def enter_common_room(character):
    affichage_lettre_par_lettre("\nYou follow the prefects through the castle corridors...")
    houses_data = load_file("src/data/houses.json")

    player_house = character.house.nom

    if player_house and player_house in houses_data:
        house_info = houses_data[player_house]

        affichage_lettre_par_lettre(f"Description of the {player_house} Common Room:")
        affichage_lettre_par_lettre(house_info.get('description', 'A majestic common room.'))

        affichage_lettre_par_lettre(house_info.get('welcome_message', f"Welcome to the noble House of {player_house}."))

        colors = ", ".join(house_info.get('colors', ['unknown']))
        affichage_lettre_par_lettre(f"Your house colors: {colors}")
    else:
        affichage_lettre_par_lettre("Could not find information for your house. Something is wrong!")


def welcome_message():
    affichage_lettre_par_lettre("Welcome, new students! Before the feast, I must say a few words.")
    affichage_lettre_par_lettre("Nitwit! Blubber! Oddment! Tweak!")
    affichage_lettre_par_lettre("Now, let the feast begin and the Sorting Ceremony commence!")
    input()

def start_chapter_2(character):

    meet_friends(character)
    welcome_message()
    sorting(character)
    enter_common_room(character)

    affichage_lettre_par_lettre(f"End of ch 2 {character.house.nom} student")
    affichage_lettre_par_lettre("="*50)

    character.display_character()
    affichage_lettre_par_lettre("End of Chapter 2! Classes begin tomorrow. Your adventure continues...")


if __name__ == "__main__":
    perso = charger_personnage()
    start_chapter_2(perso)