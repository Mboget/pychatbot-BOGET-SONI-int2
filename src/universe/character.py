################################# Creation and management of the player #################################

class Character:
    def __init__(self, last_name:str, first_name:str, attributes:dict):
        self.last_name = last_name
        self.first_name = first_name
        self.money = 100
        self.inventory = []
        self.spells = []
        self.attributes = attributes.copy() #pour éviter les bugs liés à la référence

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
        self.key.append(item) # type: ignore

"""
mes_attribues = {
    "courage" : 8,
    "intelligence" : 8,
    "loyalty" : 8,
    "ambition" : 8
}
perso = Character("BOGET","Mathieu",mes_attribues)
perso.display_character()
"""
    