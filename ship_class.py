# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:38:01 2020

@author: jenpr
"""

"""Creating ship - this is the central hub for the game. Players will start here following the introduction. This class provides access to other classes - equipment inventory/planet inventory/equipment choice/planet choice."""

class Ship:
    #class variables:
    __helptip = "The ship is your central hub for the game. Here you can look at your equipment inventory, find information about planets, get updates on your progress in the game, choose your mission and choose your equipment."
    """class methods for ship"""
    def __init__(self, name, equipment, planets, status, missions, armory):
        #instance variables
        self.__name = name
        self.__equipment = equipment
        self.__planets = planets
        self.__status = status
        self.__misions = missions
        self.__armory = armory 
    
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    
    @classmethod
    def helptp(cls):
        return cls.__helptip