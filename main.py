# coding: utf-8
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
    pygame.init()
    game = Level()


    window = game.window_generation()
    map_structure = game.get_labyrinth_structure()
    mcgyver = Character(map_structure)

    game_continue = 1
    while game_continue:
        game.set_labyrinth(window)
        pygame.time.Clock().tick(10)
        for event in pygame.event.get():
            if event.type == QUIT:
                game_continue = 0
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
        window.blit(mcgyver.image, (mcgyver.position))
        pygame.display.flip()   #Screen refresh

        if game.level_structure[mcgyver.abscissa][mcgyver.ordinate] == "G":
            game_continue = 0
            print('WIN')
            # Now we need to set a win condition
            # If number of items = 3, victory
            # Else, lose, YOU DEAD
if __name__ == "__main__":
    main()
