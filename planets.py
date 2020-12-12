# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:04:58 2020

@author: jenpr
"""

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
    
    def Identify(self):
        print(self.__name)
        return self.__name
    
    def introducePlanet(self): 
        print(self.__description)
        return self.__description
    
    def dangerLevel(self):
        print(self.__danger)
        return self.__danger
    
    
def pickPlanets():
    print("Here are planet options you have")

    planets_inventory=[]

    planet1 =planets("Wilderness", "A planet with small villages.The intelligence we have indicates that someone in the village has information about the evil plan and knowledge of where to find more clues. This planet has many places for enemies to hide and construct their plans. You never know what clues you might find left behind. " )
    planet1.Identify()
    planet1.introducePlanet()
    planets_inventory.append(planet1)

    planet2 = planets("City", "Urban planet at the center of the galaxy’s trade and government. Many important people live and work here, but you never know what is hiding in back alleys.")
    planet2.Identify()
    planet2.introducePlanet()
    planets_inventory.append(planet2)

    print("Input between Wilderness and City for the planet of your choice")
    planet = input("Insert your planet")
    print("And your planet is", planet) 

