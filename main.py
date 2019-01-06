# coding: utf-8
"""
    This will contains the main script for the McGyver Labyrinth Game
    First we gonna start to set up a basic non object code
"""

#Pygame and classes/constants import
#Window initialisation

import pygame
from pygame.locals import *
from classes import character, items, level
from constants import NEEDLE, ETHER, TUBE

def main():
    """
        Main Method
    """
    pygame.init()

    #Generating Window
    game = level.Level()
    window = game.window_generation()
    #Generating Home Menu
    home = 1
    home_image = pygame.image.load("images/mcgyver_home.png").convert()
    #Generating Labyrinth Structure
    map_structure = game.get_labyrinth_structure()
    #Generating Character
    mcgyver = character.Character(map_structure)
    #Generating Items
    needle_item = items.Item(map_structure, NEEDLE)
    ether_item = items.Item(map_structure, ETHER)
    tube_item = items.Item(map_structure, TUBE)
    needle_item.item_position("needle")
    ether_item.item_position("ether")
    tube_item.item_position("tube")
    item_number = 0

    while home:
        window.blit(home_image, (0, 0))  # displaying home screen
        pygame.display.flip()  # window refreshing
        game_continue = 0
        for event in pygame.event.get():
            if event.type == 12: # QUIT
                home = 0
                game_continue = 0
            elif event.type == 2:
                if event.key == 32:
                    home = 0
                    game_continue = 1
        while game_continue:
            window.fill(0) # Erase the window the clean the item images
            game.set_labyrinth(window)
            pygame.time.Clock().tick(10)
            for event in pygame.event.get():
                if event.type == 12: # QUIT
                    game_continue = 0
                elif event.type == 2: # KEYDOWN
                    if event.key == 27: # K_ESCAPE
                        game_continue = 0
                    else:
                        mcgyver.move(event.key)

            needle_item.display(window, "needle", item_number)
            ether_item.display(window, "ether", item_number)
            tube_item.display(window, "tube", item_number)

            window.blit(mcgyver.image, (mcgyver.position))
            pygame.display.flip()   #Screen refresh

            if game.level_structure[mcgyver.abscissa][mcgyver.ordinate] == "G":
                game_continue = 0
                if item_number == 3:
                    print('WIN')
                else:
                    print('Loose, you only got ' + str(item_number) + " on 3, try again")
            elif mcgyver.position == ether_item.position and ether_item.got_item is False:
                print('Yes i got an item! That\'s ether!')
                item_number += 1
                ether_item.got_item = True
            elif mcgyver.position == needle_item.position and needle_item.got_item is False:
                print('Yes i got an item! That\'s a needle!')
                item_number += 1
                needle_item.got_item = True
            elif mcgyver.position == tube_item.position and tube_item.got_item is False:
                print('Yes i got an item! That\'s a tube!')
                item_number += 1
                tube_item.got_item = True

if __name__ == "__main__":
    main()
