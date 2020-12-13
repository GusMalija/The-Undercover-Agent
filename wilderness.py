# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 23:29:02 2020

@author: jenpr
"""
"""wilderness class. Establishes, class, objects and functions related to the wilderness planet. In the future, the functions and outcomes will be dependent on the equipment in the player's inventory, but not at this moment."""

#player obtains clue about the enemy from the villagers
"""Wilderness planet as the parent class"""
   


from ship_class import welcomeback
from tictactoe import tictactoe
from slowprint import slowdown

"""Wilderness planet as the parent class"""        
class Wilderness:
  def __init__(self, village, villagers):
    self.__village = village
    self.__villagers = villagers
   
    """function to print introductory text and provide choice of where on the planet to go"""    
    

"""marketplace as a child class ineherits from wilderness"""
class marketplace(Wilderness):
  def __init__(self, bags, WaterCan):
    self.__bags = bags
    self.__WaterCan = WaterCan
  
  """creating a method for the agent to obtain information about the enemy from the marketplace"""
  def AskVillagers(self):
      converse_options = ["1", "2"]
      user_choice = ""
      while user_choice not in converse_options:
         slowdown("\nYou decide to ask the villagers some questions. You approach a fruit vendor and decide to question them. \nWhich approach will you choose? \n 1)Hello. Have you had any unusual visitors recently? \n 2)Have you see anything suspicious lately?")
         user_choice = str(input("Enter option number: "))
      if user_choice == converse_options[0]:
         slowdown("Vendor: 'Yes, actually. A suspicious man bought"  + str(self.__bags) + " bags of cereal and" + str(self.__WaterCan) + "Water can. He went filling his water can at the watering hole then disappeared to the forest'")
      elif user_choice == converse_options[1]:
         slowdown("\nVendor: 'What do you mean by suspicious? How do I know you aren't suspicious? Find someone else to talk to.'")
         slowdown("\nYou decide to try again. You approach another villager. You ask her if she's seen any new visitors lately.")
         slowdown("\nVillager: 'Yes, actually. I saw a suspicious man buy "  + str(self.__bags) + " bags of cereal and " + str(self.__WaterCan) + " Water can. He went to fill his water can at the watering hole.'")                  
         input("\n\nPress the enter key to continue.")
"""function to get information from villagers to find the last clue."""
def wateringHole():
    slowdown("\n\nYou decide to see if anyone near the watering hole remembers the stranger.")
    slowdown("\nYou see a woman filling a jug with water and ask if she saw anyone recently. \n Villager: 'Yes, actually. It was strange. A man was getting a drink and speaking on a communicator. He mentioned something about 2 weeks but I don't know what. I did see him head to the forest after, though.' \n You thank the villager and head to the forest.")
    input("\n\nPress the enter key to continue")
    
""" function which uses the class method ask villagers to specify the number of items villagers saw the enemy to posess"""
def seehowmany():
   library = marketplace(2,1)
   library.AskVillagers()


"""function to print string describing the village"""
def lookAround():
   slowdown("You see villagers buying their daily groceries and vendors trying to catch your attention with their products.")
      
"""forest as a child class of wilderness"""
class forest(Wilderness):
  def __init__(self, leaves, wallet):
    self.__leaves = leaves
    self.__wallet = wallet
   
  
#he comes accross a bunch of leaves and thinks it is where the enemy slept for warmth. He excavates it out of curiosity    
  def excavate(self):
      slowdown("It's great that you excavated " + str(self.__leaves) + "bunch of leaves because the enemy used it as a chill spot. The " + str(self.__wallet) + " wallet you found has their finger prints, and what looks like a coded message.")

    
"""function which uses the class method excavate to specify a number of items the agent has found in the forest exploration"""  
  
def findhowmany():
    library = forest(1,1)
    library.excavate()#agent steps into the forest in hopes to catch the enemy



"""sequence for landing on the planet. sends you to the village"""
def wildIntro():
    slowdown('''You have landed on the Wilderness planet.   
You can see a village with a bustling marketplace, and a forest in the far distance. You decide to start in the village.''')
    visitMarket()      
 

        
"""function to visit marketplace"""
def visitMarket():
    slowdown("\n \nYou walk into the village, alert for signs of trouble. People look surprised to see a stranger. If the intergalactic trouble-makers were here, the villagers would probably remember them.")
    lookAround()
"""function to visit forest and investigate, uses class methods"""
def visitForest():
    slowdown("\n\n Now that you've found information in the village, you begin to walk through the dark trees beyond the village. ")
    explore_options = ["1","2"]
    user_choice =""
    while user_choice not in explore_options:
        slowdown("\nYou see what looks like be a clearing in the forest to your right and a river to your left.\n You choose to turn \n1) right towards the clearing. \n2) left towards the river.")
        user_choice =str(input("Enter your option number: "))
    if user_choice ==explore_options[0]:
        clearingLook()
    if user_choice ==explore_options[1]:
        slowdown("You follow the river, but the water seems to have washed away any evidence that might have existed. \n You decide to turn back and explore the clearing.")
        input("\n\nPress the enter key to continue")
        clearingLook()   

"""function to use forest class methods to explore the forest"""
def clearingLook():
      slowdown("You see the remains of a fire and some piles of leaves.")
      lookat = ["1","2"]
      user_choice = ""
      while user_choice not in lookat:
          slowdown("\nWhat do you want to excavate? \n1)The fire. \n2) The leaves.")
          user_choice = str(input("Enter option number: "))
      if user_choice == lookat[0]:
          slowdown("\nYou dig through the ashes of the fire but find nothing. You decide to look at the leaves.")
          findhowmany()  
      elif user_choice == lookat[1]:
          findhowmany()
          input("\n\nPress the enter key to continue.")   
          slowdown("\nBefore heading back to your ship, you must decode the clue.")



    