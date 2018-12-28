# -*- coding: Utf-8 -*
"""
    This will contains the main script for the McGyver Labyrinth Game
    First we gonna start to set up a basic non object code
"""

#Pygame and classes/constants import
#Window initialisation

import pygame
from pygame.locals import *

from classes import *
from constants import *

def main():
    """
        Main Method with object
    """
    #Generating Map
    game = Level()
    map_structure = game.get_labyrinth_structure()
    window = game.window_generation()
    game.set_labyrinth(window)
    #Generating Character
    mcgyver = Character(map_structure)

    level_continue = 1
    while level_continue:
        pygame.time.Clock().tick(10)
        for event in pygame.event.get():
            if event.type == QUIT:
                level_continue = 0
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    level_continue = 0
                elif event.key == K_RIGHT:
                    mcgyver.move('right')
                elif event.key == K_LEFT:
                    mcgyver.move('left')
                elif event.key == K_UP:
                    mcgyver.move('up')
                elif event.key == K_DOWN:
                    mcgyver.move('down')
        game.set_labyrinth(window)
        window.blit(mcgyver.position, (mcgyver.pixel_x, mcgyver.pixel_y))
        pygame.display.flip()   #Screen refresh

        if game.level_structure[mcgyver.abscissa][mcgyver.ordinate] == "G":
            #End of the game, Victory
            print('WIN MA NEGA')
            #Now we need to set a win condition
            #If number of items = 3, victory
            #Else, lose, YOU DEAD NEGA
main()
