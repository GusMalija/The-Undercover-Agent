# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:47:02 2020

@author: jenpr
"""

"""introduction to the game. Strings. Establish character using user input. Introduce user to the rules and world of the game."""

from slowprint import slowdown
def intro(): 
    slowdown("Welcome to Undercover Agent – A mission to save the galaxy ")
    name=input("Insert your name")
    print("\nHello Agent",name)
    input("\n\nPress the enter key to continue to the rules of the game.")

    #Rules of the game 
    slowdown("\n\n These are rules of the game")
    slowdown("\n\nRule 1. The theme of the game is mysterious & adventurous. You must pick equipment based on how you envision this adventurous game to go in order to save the galaxy.")
    input("\n\nPress the enter key to continue to the next rule.")

    slowdown("\n\nRule 2. The game escalates based on levels, each level will unlock as you finish one level")
    input("\n\nPress the enter key to continue to the next rule.")

    slowdown("\n\nRule 3. You will be awarded points based on how successful you are on every level of the game. The highest point is 5 and the lowest is 0")
    input("\n\nPress the enter key to continue to continue to the last rule.")

    slowdown("\n\nRule 4. Once you start the game, you will have to finish it. There is no turning back")
    input("\n\nPress the enter key to continue to your mission.")


    #About the game 
    slowdown("\nAbout the Galaxy: The galaxy has been at peace for 100 years. But intelligence has been gathered indicating that there are forces trying to destroy that peace, and with it, the galaxy itself! Your mission is to travel the galaxy, make contacts and gather clues in order to stop their evil plan in its tracks and save the galaxy.")
    input("\n\nPress the enter key to continue.")

    #Building the game 
    slowdown("\nThis is your ship. As you endeavor to save the galaxy, this ship will be your central hub. From here, you can check your equipment inventory, find information about the planets you may be traveling to, choose your equipment and choose your destination.")
    slowdown("\nAre you ready to start exploring your ship?")
    input("\n\nPress the enter key to continue.")

    slowdown("\nYour first stop on the ship is your equipment inventory. We will look at your equipment now.")
    input("\n\nPress the enter key to continue")


