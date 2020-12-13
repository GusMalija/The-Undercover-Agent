# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:09:34 2020

@author: jenpr
"""

"""creates class for city planet"""
#At Hamburg, the highlight is the concert house. Apartnments are surreal and expensive, people living there are known to be boogy
class City:
   def __init__(self, DownTown):
     self.__DownTown = DownTown
#agent meets a group of people in a bar and strikes a conversation
class Bar(City):
  def __init__(self, room, weeks):
    self.__room = room
    self.__weeks = weeks

#one person spits out gold for the agent
  def conversation(self):
    print("I have heared of a suspicious man renting" + str(self.__room) +"appartment at the Hamburg concert house. He has been living there for" + str(self.__weeks) + "weeks now")


library = Bar(1, 2)
library.conversation()

class ConcertHouse(City):
  def __init__(self, BombAlert, residents):
    self.__BombAlert = BombAlert
    self.__residents = residents
  def capture(self):
    print("Police issues" + str(self.__BombAlert) + " Bomb alert announcement to evacuate" + str(self.__residents) + "inhabitants of the building. Agent identifies and arrests the new resident. He really was the enemy. Poor enemy!")

library = ConcertHouse(1, 7)
library.capture()