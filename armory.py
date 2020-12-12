# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:04:47 2020

@author: jenpr
"""

from equipment_general import Item_equipment
from inventory import equipInventory
from inventory import printList

"""creates objects and functions for choosing equipment"""
class Pick:
  
  def __init__(self, capacity=3):
    self.__capacity = capacity
    self.__items = []

  def addItem(self, item):
    if len(self.__items) <= self.__capacity:
      print("Sure, item" + item + " is in your posession")
      self.__items.append(item)
    else: 
      print("Unfortunately, you can't pick more")

"""function to choose equipment items"""
def fillBackpack():
    backpack = Pick()
    choice1 =input("Make your first choice from the inventory list")
    print(choice1)
    backpack.addItem(choice1)

    choice2 = input("Make your second choice from the inventory list")
    print(choice2)
    backpack.addItem(choice2)

    choice3 = input("Make your third choice from the inventory list")
    print(choice3)
    backpack.addItem(choice3)