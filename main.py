# coding: utf-8
"""
    This will contains the main script for the McGyver Labyrinth Game
    First we gonna start to set up a basic non object code
"""

#Pygame and classes/constants import
#Window initialisation

import pygame
from pygame.locals import *
from classes import Level, Character, Item

def main():
    """
        Main Method
    """
    #Generating Map
    pygame.init()
    game = Level()

    window = game.window_generation()
    map_structure = game.get_labyrinth_structure()
    mcgyver = Character(map_structure)


    aiguille_item = Item(map_structure)
    ether_item = Item(map_structure)
    tube_item = Item(map_structure)
    seringue_item = Item(map_structure)
    aiguille_item.item_position("aiguille")
    ether_item.item_position("ether")
    tube_item.item_position("tube")

    home = 1
    home_image = pygame.image.load("images/mcgyver_home.png").convert()

    item_number = 0
    got_ether = False
    got_tube = False
    got_aiguille = False

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
                    print(event.key)
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
            if got_aiguille is False:
                window.blit(aiguille_item.aiguille_image, (aiguille_item.position))
            elif item_number < 3:
                window.blit(aiguille_item.aiguille_image, [0, 450])
            if got_ether is False:
                window.blit(ether_item.ether_image, (ether_item.position))
            elif item_number < 3:
                window.blit(ether_item.ether_image, [40, 450])
            if got_tube is False:
                window.blit(tube_item.tube_image, (tube_item.position))
            elif item_number < 3:
                window.blit(tube_item.tube_image, [80, 450])
            if item_number == 3:
                window.blit(seringue_item.seringue_image, [0, 450])

            window.blit(mcgyver.image, (mcgyver.position))
            pygame.display.flip()   #Screen refresh

            if game.level_structure[mcgyver.abscissa][mcgyver.ordinate] == "G":
                print(mcgyver.position)
                game_continue = 0
                if item_number == 3:
                    print('WIN')
                else:
                    print('Loose, you only got ' + str(item_number) + " on 3, try again")
            elif mcgyver.position == ether_item.position and got_ether is False:
                print('Yes i got an item! That\'s ether!')
                item_number += 1
                got_ether = True
            elif mcgyver.position == aiguille_item.position and got_aiguille is False:
                print('Yes i got an item! That\'s an aiguille!')
                item_number += 1
                got_aiguille = True
            elif mcgyver.position == tube_item.position and got_tube is False:
                print('Yes i got an item! That\'s a tube!')
                item_number += 1
                got_tube = True


if __name__ == "__main__":
    main()
