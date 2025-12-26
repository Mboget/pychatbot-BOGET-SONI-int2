################################# Creation and management of the player #################################
from src.universe.house import House 
from src.utils.input_utils import ask_choice

class Character:
    def __init__(self, last_name:str, first_name:str, attributes:dict, money = 100, inventory = [], spells = [], house = House()):
        self.last_name = last_name
        self.first_name = first_name
        self.money = money
        self.inventory = inventory
        self.spells = spells
        self.attributes = attributes.copy() 
        self.house = house

    def display_character(self):
        print(f"Character profile: ")

        print(f"Last name: {self.last_name}")
        print(f"First name : {self.first_name}")
        print(f"Money : {self.money}")
        print("Inventory :", *(f"- {element}" for element in self.inventory), sep="\n")
        print("Spells :", *(f"- {element}" for element in self.spells), sep="\n")
        print("Attributes :", *(f"- {attribute} : {level}" for attribute,level in self.attributes.items()), sep="\n")

    def add_item(self,key,item): 
        assert key in ['inventory','spells']
        if key == 'inventory':
            self.inventory.append(item) # type: ignore
        elif key == 'spells':
            self.spells.append(item)
        else : 
            print("NIKTAMERE sale caca")

    def house_choice(self,questions):
        houses = ["Gryffindor","Slytherin","Hufflepuff","Ravenclaw"]
        houses_score = {
                "Gryffindor" : self.attributes["courage"]**2,
                "Slytherin" : self.attributes["ambition"]**2,
                "Hufflepuff" : self.attributes["loyalty"]**2,
                "Ravenclaw" : self.attributes["intelligence"]**2
        }

        for question in questions:

            score_house = ask_choice(question[0],question[1])
            name_house = houses[score_house] # type: ignore
            houses_score[name_house] += score_house

        return houses_score
