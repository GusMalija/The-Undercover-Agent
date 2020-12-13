# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:04:58 2020

@author: jenpr
"""
from slowprint import slowdown
"""creates class for planet database"""
class planets: 
    def __init__(self, name, description, danger="", choose=False):
        self.__name= name
        self.__description= description
        self.__danger = danger
        self.__choose = choose
        
        
    def setName(self):
        self.__name
    def getName(self, name):
        return name 
    """function to identify the planet name"""
    def Identify(self):
        slowdown(self.__name)
        return self.__name
    """function to provide the description of the planet"""
    def introducePlanet(self): 
        slowdown(self.__description)
        return self.__description
    """function to identify how dangerous the planet is"""
    def dangerLevel(self):
        slowdown(self.__danger)
        return self.__danger
    
"""function to pick which planet to travel to"""    
def pickPlanets():
    slowdown("Here are planet options you have")

    planets_inventory=["1","2"]
    user_choice=""
    
    planet1 =planets("Wilderness", "A planet with small villages.The intelligence we have indicates that someone in the village has information about the evil plan and knowledge of where to find more clues. This planet has many places for enemies to hide and construct their plans. You never know what clues you might find left behind. " )
    planet1.Identify()
    planet1.introducePlanet()
    planets_inventory.append(planet1)

    planet2 = planets("City", "Urban planet at the center of the galaxy’s trade and government. Many important people live and work here, but you never know what is hiding in back alleys.")
    planet2.Identify()
    planet2.introducePlanet()
    planets_inventory.append(planet2)
    
    while user_choice not in planets_inventory:
        slowdown("Choose between 1) Wilderness and 2) City for the planet of your choice")
        user_choice= str(input("Insert your number choice: "))
    if user_choice== planets_inventory[0]:
        print("Your destination is Planet Wilderness.")
    elif user_choice== planets_inventory[1]:
        print("Your destination is Planet City.") 

pickPlanets()
