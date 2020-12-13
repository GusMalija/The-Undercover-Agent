"""
Created on Tue Nov 10 14:42:12 2020

@author: jenpr
"""

"""class for equipment that can be used in the game. includes functions related to the items"""
from slowprint import slowdown

class Item_equipment: 
    from slowprint import slowdown
    """slow down the speed at which text is printed"""
    
    """
    Equipment: description attribute, and a method that returns the description or uses
    """
    def __init__(self, name, description, isGoodFor, observe="", audio="", EnemyFights=False,isEvidence=False, Blade=False,isAlien=False, isDoorLocked=False, isAttractiveEnemyAlly=False):
        self.__name = name
        self.__description = description
        self.__isGoodFor = isGoodFor
        self.__uses = ""
        self.__observe = observe
        self.__EnemyFights = EnemyFights 
        self.__Blade = Blade
        self.__isAlien = isAlien
        self.__isDoorLocked = isDoorLocked
        self.__isAttractiveEnemyAlly = isAttractiveEnemyAlly
        self.__audio = audio
        self.__isEvidence = isEvidence
        

    """function to set name and get name for use in future code"""
    def setName(self):
        self.__name 
    def getName(self, name):
        return self.__name 
    """function to report the name of specific items in inventory"""
    def category(self):
        #slowdown(self.__name)
        return self.__name
    """function to return the description of the item in inventory"""
    def introduceItem(self): 
        #slowdown(self.__description)
        return self.__description
    """function to identify what the item can be used for"""
    def whatFor(self):
        #slowdown(self.__isGoodFor)
        return self.__isGoodFor
    
    """function to print lists and items"""
    def printItem(self):
        slowdown(self.__name + "\n")
        slowdown(self.__description + "\n")
        slowdown(self.__isGoodFor)
        return self.__name, self.__description, self.__isGoodFor
    
  
   
#The agent has to pick equipment - actions
       
    """functions to add available actions with which to use equipment"""
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
            print("Deceive her with the necklace")
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
                
   #inspecting equipment - not yet picking

