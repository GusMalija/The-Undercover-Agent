# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:04:58 2020

@author: jenpr
"""

class planets: 
    def __init__(self, name, description, danger="", choose=False):
        self.__name__ = name
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
    
    def flyTo(self):
        pass #Code choice of planet here
        

planet_inventory =[]

planet1 = planets("Wilderness", "")
planet1.Identify()
planet1.introducePlanet()
planet1.dangerLevel()
planet_inventory.append(planet1.takeItem())

#Complete planet list for wilderness, city, water and desert planets
