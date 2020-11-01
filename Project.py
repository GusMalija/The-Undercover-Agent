# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 23:44:33 2020

@author: user
"""

print("Welcome to Undercover Agent – A mission to save the galaxy ")
name=input("Insert your name")
print ("Hello Agent",name)

#Rules of the game 
print("Here are rules of the game")
print("Rule 1. The theme of the game is mysterious, pick equipments based on how you envision this adventurous game to go")
print("Rule 2. The game escalates based on levels, each level will unlock as you finish one level")
print("Rule 3. You will be awarded points based on how successful you are on every level of the game. The highest point is 5 and the lowest is 0")
print("Rule 4. Once you start the game, you will have to finish it. There is not turning back")


#About the game 
print("About the Galaxy: The galaxy has been at peace for 100 years. But intelligence has been gathered indicating that there are forces trying to destroy that peace, and with it, the galaxy itself! Your mission is to travel the galaxy, make contacts and gather clues in order to stop their evil plan in its tracks and save the galaxy.")

#Building the game 

class Item: 
    """
    description attribute, and a method that returns the description
    """
    def __init__(self, description,RayGun, observe,audio, EnemyFights=False,isEvidence=False, Blade=False,isAlien=False, isDoorLocked=False, isAttractiveEnemyAlly=False):
        self.__description = description
        self.__RayGun = RayGun
        self.__uses = []
        self.__observe = observe
        self.__EnemyFights = EnemyFights 
        self.__Blade = Blade
        self.__isAlien = isAlien
        self.__isDoorLocked = isDoorLocked
        self.__isAttractiveEnemyAlly = isAttractiveEnemyAlly
        self.__audio = audio
        self.__isEvidence = isEvidence
        
    #The agent has to pick equipment

    def lookAt(self):
      look = self.__description
      if  self.__isDoorLocked:
          look += " Unlock using the blade"
      print(look)    
            
    def use(self):
       if self.__EnemyFights:
           print("Enemy is strong")
           if self.__RayGun:
             print("shoot him with a gun")
           else:
             print("reserve your gun")
     
    def Spray(self):
        print(self.__observe)
        if self.__isAlien:
            print("Spray them with knock-out gas")
        else:
            print("knock-out gas is not a good option")
            
    def bribe (self):
        if self.__isAttractiveEnemyAlly:
            print("Decieve her with the necklace")
        else:
            print("Reserve that for another fine lady")
        
    def shoot(self):
        if self.__EnemyFights:
            print("shoot him with a gun")
        else:
            print("reserve your gun")
    def record(self):
        if self.__isEvidence:
            if self.__audio:
                print("Use your audio recorder")
            else:
                print("no audio evidence")
      
      

      
      
      
      