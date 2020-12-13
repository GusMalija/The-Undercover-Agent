# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:03:44 2020

@author: jenpr
"""

from introduction import intro
from slowprint import slowdown
import inventory
"""importing equipment module to enable a review of the inventory"""
import equipment_general
"""importing equipment module to enable a review of the inventory"""
from inventory import printList

print(intro())
printList()
slowdown("Now we will look at two locations where there have been rumors of trouble.")
input("\n\nPress the enter key to continue")
import planets
from planets import pickPlanets
pickPlanets()
slowdown("Now to equip you for your mission. You can refer back to the Inventory for your options.")
import armory
from armory import fillBackpack
fillBackpack()
slowdown("Well, now that you are equiped and have your destination ready, we will journey to your first destination.  I wish you luck, Agent.")
import wilderness
from wilderness import wildIntro
from wilderness import seehowmany
from wilderness import visitForest
from wilderness import wateringHole
from wilderness import marketplace
from wilderness import forest
from ship_class import welcomeback
from tictactoe import tictactoe
wildIntro()
seehowmany()
wateringHole()
visitForest()
"""player must beat minigame to move forward"""
tictactoe()
slowdown("Now that you've decoded the clue, you should head back to your ship as quickly as possible!")
welcomeback()








   
