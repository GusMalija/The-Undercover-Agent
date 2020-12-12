# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:03:44 2020

@author: jenpr
"""

from introduction import intro
import Base
import slowprint
import inventory
"""importing equipment module to enable a review of the inventory"""
import equipment_general
"""importing equipment module to enable a review of the inventory"""
from inventory import printList

print(intro())
printList()
print("Now we will look at two locations where there have been rumors of trouble.")
input("\n\nPress the enter key to continue")
import planets
from planets import pickPlanets
pickPlanets()
print("Now to equip you for your mission. You can refer back to the Inventory for your options.")
import armory
from armory import fillBackpack
fillBackpack()
print("Well, now that you are equiped and have your destination ready, we will journey to your first destination.  I wish you luck, Agent.")







   
