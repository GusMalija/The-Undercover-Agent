# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:47:16 2020

@author: jenproch

equipment inventory - users will use class methods to pull information about inventory"""

#import equipment general

from equipment_general import Item_equipment


equip_inventory = []

item1 = Item_equipment("Ray-Gun", "Versatile and strong weapon.", "Useful against all enemies.")
item1.category()
item1.introduceItem()
item1.whatFor()
equip_inventory.append(item1.takeItem())


item2 = Item_equipment("Blade", "Always sharp and easily hidden.", "Useful against weaker enemies and locked doors.")
item2.category()
item2.introduceItem()
item2.whatFor()
equip_inventory.append(item2.takeItem())

item3 = Item_equipment("Knock-Out Gas", "Aerosol that can stun and knock-out opponents.", "Useful for weakening opponents or sneaking past guards.")
item3.category
item3.introduceItem()
item3.whatFor()
equip_inventory.append(item3.takeItem())

item4 = Item_equipment("Diamond Necklace", "Exceptionally shiny, worth a great deal on all planets.", "Useful for charming or bribing.")
item4.category()
item4.introduceItem()
item4.whatFor()
equip_inventory.append(item4.takeItem())

item5 = Item_equipment("Jeweled, titanium watch", "Watch made of prized metals and jewels.", "Useful for charming, bribing or telling time.")
item5.category()
item5.introduceItem()
item5.whatFor()
equip_inventory.append(item5.takeItem())

item6 = Item_equipment("Seeds", "Able to grow into edible plants in any soil.", "Useful if you get stuck without food.")
item6.category()
item6.introduceItem()
item6.whatFor()
equip_inventory.append(item6.takeItem())

item7 = Item_equipment("Fertilizer", "Can be used to speed up growth of seeds or strengthen explosions.", "Useful for quickly satisfying hunger or building a bigger bomb.")
item7.category()
item7.introduceItem()
item7.whatFor()
equip_inventory.append(item7.takeItem())

item8 = Item_equipment("Camera", "Bulky but capable of recording video and still photos.", "Useful for recording visual evidence, but can't be easily hidden.")
item8.category()
item8.introduceItem()
item8.whatFor()
equip_inventory.append(item8.takeItem())

item9 = Item_equipment("Audio-Recorder", "Small and capable of recording audio.", "Useful for recording audio evidence and can be easily hidden.")
item9.category()
item9.introduceItem()
item9.whatFor()
equip_inventory.append(item9.takeItem())

item10 = Item_equipment("Dress Suit", "Profession suit of clothing.", "Useful for fancy parties and charming contacts.")
item10.category()
item10.introduceItem()
item10.whatFor()
equip_inventory.append(item10.takeItem())

item11 = Item_equipment("Armor", "Full defensive set of equipment.", "Import to defend yourself from attack while in search of clues.")
item11.category()
item11.introduceItem()
item11.whatFor()
equip_inventory.append(item11.takeItem())

item12 = Item_equipment("Deck of cards", "A set of playing cards adaptable to all social settings.", "Good for breaking the ice and extracting information.")
item12.category()
item12.introduceItem()
item12.whatFor()
item15.introduceItem()
equip_inventory.append(item12.takeItem())

item13 = Item_equipment("License", "Universal license to operate machinery wherever you may go", "Good for acquiring a vehicle if needed.")
item13.category()
item13.introduceItem()
item13.whatFor()
equip_inventory.append(item13.takeItem())

item14 = Item_equipment("Breathing Device", "Breathing apparatus that can be used underwater or in low oxygyen environments.", "Good for surviving in hostile environments.")
item14.category()
item14.introduceItem()
item14.whatFor()
equip_inventory.append(item14.takeItem())

item15 = Item_equipment("First Aid Kit", "Contains healing devices and equipment.", "Good for treating injuries.")
item15.category()
item15.whatFor()
equip_inventory.append(item15.takeItem())

item16 = Item_equipment("Plant Identifier", "Device that contains information about a universal selection of plants, including information about nutrition and poisonous qualities.", "Good for figuring out which plants will feed you or kill you.")
item16.category()
item16.introduceItem()
item16.whatFor()
equip_inventory.append(item16.takeItem())



if input("inventory"):
    print(equip_inventory)