"""
Created on Tue Nov 10 14:42:12 2020

@author: jenpr
"""

class Item_equipment: 
    """
    Equipment: description attribute, and a method that returns the description or uses
    """
    def __init__(self, name, description, isGoodFor, observe="", audio="", EnemyFights=False,isEvidence=False, Blade=False,isAlien=False, isDoorLocked=False, isAttractiveEnemyAlly=False):
        self.__name__ = name
        self.__description= description
        self.__isGoodFor = []
        self.__uses = []
        self.__observe = observe
        self.__EnemyFights = EnemyFights 
        self.__Blade = Blade
        self.__isAlien = isAlien
        self.__isDoorLocked = isDoorLocked
        self.__isAttractiveEnemyAlly = isAttractiveEnemyAlly
        self.__audio = audio
        self.__isEvidence = isEvidence
        

    def setName(self):
        self.__name 
    def getName(self, name):
        return self.__name 
    
    def category(self):
        print(self.__name)
        return self.__name
    
    def introduceItem(self): 
        print(self.__description)
        return self.__description
    
    def whatFor(self):
        print(self.__isGoodFor)
        return self.__sGoodFor
    

   
#The agent has to pick equipment - actions
       
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

