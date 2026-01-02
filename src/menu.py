################################# manages the main menu #################################

# menu.py

from src.chapters.chapter_1 import start_chapter_1
from src.chapters.chapter_2 import start_chapter_2
from src.chapters.chapter_3 import start_chapter_3
from src.chapters.chapter_4 import start_chapter_4

from src.universe.house import House
from src.utils.input_utils import charger_personnage
from src.utils.input_utils import affichage_lettre_par_lettre

def display_main_menu():
    print("\n" + "=" * 40)
    affichage_lettre_par_lettre("🧙‍♂️ WELCOME TO THE HARRY POTTER GAME 🧙‍♂️")
    print("=" * 40)
    affichage_lettre_par_lettre("1. Start Chapter 1 – Arrival in the magical world")
    affichage_lettre_par_lettre("2. Exit the game")
    print("=" * 40)


def launch_menu_choice():

    houses = [House("Gryffindor"),House("Slytherin"),House("Hufflepuff"),House("Ravenclaw")]

    running = True

    while running:
        display_main_menu()
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            print("\n✨ The adventure begins...\n")

            start_chapter_1()

            perso = charger_personnage()

            start_chapter_2(perso)

            start_chapter_3(perso)

            start_chapter_4(perso,houses)

            print("\n🏆 FINAL HOUSE POINTS 🏆")
            for house in houses:
                print(f"{house.afficher_point()}")

            print("\nThank you for playing! ⚡")
            running = False

        elif choice == "2":
            print("\n👋 Goodbye, young wizard. See you at Hogwarts!")
            running = False

        else:
            print("\n❌ Invalid choice. Please enter 1 or 2.")

    