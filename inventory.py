# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:47:16 2020

@author: jenproch

equipment inventory - users will use class methods to pull information about inventory"""

#import equipment general

from equipment_general import Item_equipment
from slowprint import slowdown

        
equipInventory = []

"""creating list based on item_equipment objects"""
item1 = Item_equipment("\nRaygun", "Versatile and strong weapon.", "Useful against all enemies.")
item1.category()
item1.introduceItem()
item1.whatFor()
equipInventory.append(item1)


item2 = Item_equipment("\nBlade", "Always sharp and easily hidden.", "Useful against weaker enemies and locked doors.")
item2.category()
item2.introduceItem()
item2.whatFor()
equipInventory.append(item2)

item3 = Item_equipment("\nKnock-Out Gas", "Aerosol that can stun and knock-out opponents.", "Useful for weakening opponents or sneaking past guards.")
item3.category()
item3.introduceItem()
item3.whatFor()
equipInventory.append(item3)

item4 = Item_equipment("\nDiamond Necklace", "Exceptionally shiny, worth a great deal on all planets.", "Useful for charming or bribing.")
item4.category()
item4.introduceItem()
item4.whatFor()
equipInventory.append(item4)

item5 = Item_equipment("\nJeweled, titanium watch", "Watch made of prized metals and jewels.", "Useful for charming, bribing or telling time.")
item5.category()
item5.introduceItem()
item5.whatFor()
equipInventory.append(item5)
    
item6 = Item_equipment("\nSeeds", "Able to grow into edible plants in any soil.", "Useful if you get stuck without food.")
item6.category()
item6.introduceItem()
item6.whatFor()
equipInventory.append(item6)

item7 = Item_equipment("\nFertilizer", "Can be used to speed up growth of seeds or strengthen explosions.", "Useful for quickly satisfying hunger or building a bigger bomb.")
item7.category()
item7.introduceItem()
item7.whatFor()
equipInventory.append(item7)

item8 = Item_equipment("\nCamera", "Bulky but capable of recording video and still photos.", "Useful for recording visual evidence, but can't be easily hidden.")
item8.category()
item8.introduceItem()
item8.whatFor()
equipInventory.append(item8)

item9 = Item_equipment("\nAudio-Recorder", "Small and capable of recording audio.", "Useful for recording audio evidence and can be easily hidden.")
item9.category()
item9.introduceItem()
item9.whatFor()
equipInventory.append(item9)

item10 = Item_equipment("\nDress Suit", "Profession suit of clothing.", "Useful for fancy parties and charming contacts.")
item10.category()
item10.introduceItem()
item10.whatFor()
equipInventory.append(item10)

item11 = Item_equipment("\nArmor", "Full defensive set of equipment.", "Import to defend yourself from attack while in search of clues.")
item11.category()
item11.introduceItem()
item11.whatFor()
equipInventory.append(item11)

item12 = Item_equipment("\nDeck of cards", "A set of playing cards adaptable to all social settings.", "Good for breaking the ice and extracting information.")
item12.category()
item12.introduceItem()
item12.whatFor()
equipInventory.append(item12)

item13 = Item_equipment("\nLicense", "Universal license to operate machinery wherever you may go", "Good for acquiring a vehicle if needed.")
item13.category()
item13.introduceItem()
item13.whatFor()
equipInventory.append(item13)

item14 = Item_equipment("\nBreathing Device", "Breathing apparatus that can be used underwater or in low oxygyen environments.", "Good for surviving in hostile environments.")
item14.category()
item14.introduceItem()
item14.whatFor()
equipInventory.append(item14)

item15 = Item_equipment("\nFirst Aid Kit", "Contains healing devices and equipment.", "Good for treating injuries.")
item15.category()
item15.introduceItem()
item15.whatFor()
equipInventory.append(item15)

item16 = Item_equipment("\nPlant Identifier", "Device that contains information about a universal selection of plants, including information about nutrition and poisonous qualities.", "Good for figuring out which plants will feed you or kill you.")
item16.category()
item16.introduceItem()
item16.whatFor()
equipInventory.append(item16)

def printList():
    for object in equipInventory:
        object.printItem()
    input("\n\nPress the enter key to continue")
