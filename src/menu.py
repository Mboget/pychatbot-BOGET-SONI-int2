################################# manages the main menu #################################

# menu.py

from src.chapters.chapter_1 import start_chapter_1
from src.chapters.chapter_2 import start_chapter_2
from src.chapters.chapter_3 import start_chapter_3
#from src.chapters.chapter_4 import start_chapter_4

from src.universe.house import House
from src.utils.input_utils import charger_personnage

def display_main_menu():
    """Displays the main game menu."""
    print("\n" + "=" * 40)
    print("🧙‍♂️ WELCOME TO THE HARRY POTTER GAME 🧙‍♂️")
    print("=" * 40)
    print("1. Start Chapter 1 – Arrival in the magical world")
    print("2. Exit the game")
    print("=" * 40)


def launch_menu_choice():
    """Controls the main menu loop and game progression."""

    # 1. Initialize houses dictionary
    houses = [House("Gryffindor"),House("Slytherin"),House("Hufflepuff"),House("Ravenclaw")]

    running = True

    # 2. Main menu loop
    while running:
        display_main_menu()
        choice = input("Enter your choice (1 or 2): ").strip()

        # 3.a Start the game
        if choice == "1":
            print("\n✨ The adventure begins...\n")

            # i. Chapter 1 – Character creation
            start_chapter_1()

            perso = charger_personnage()

            # ii. Chapter 2 – Journey to Hogwarts & house selection
            start_chapter_2(perso)

            # iii. Chapter 3 – Learning spells & magic quiz
            start_chapter_3(perso)

            # iv. Chapter 4 – Quidditch test or final chapter
            #start_chapter_4(perso)

            print("\n🏆 FINAL HOUSE POINTS 🏆")
            for house in houses:
                print(f"{house.afficher_point()}")

            print("\nThank you for playing! ⚡")
            running = False

        # 3.b Exit game
        elif choice == "2":
            print("\n👋 Goodbye, young wizard. See you at Hogwarts!")
            running = False

        # 3.c Invalid choice
        else:
            print("\n❌ Invalid choice. Please enter 1 or 2.")

    