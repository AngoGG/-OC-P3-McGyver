"""
    Will contain all the program classes
"""
import pygame
from pygame.locals import *
from constants import SPRITE_SIZE, SPRITES_NUMBER, MCGYVER

class Character:
    """
        Main Character class
        Generation and motion management
    """

    def __init__(self, map_structure):
        #Recupération de la position du personnage en case et en pixel
        self.abscissa = 0
        self.ordinate = 0
        self.pixel_x = 0
        self.pixel_y = 0
        self.map = map_structure
        self.image = pygame.image.load(MCGYVER).convert_alpha()

    def move(self, direction):
        """
            Make the character move
        """
        if direction == 275: # K_RIGHT
            #Check that he wont get outside the Screen
            if self.abscissa < (SPRITES_NUMBER - 1):
                #Check that he wont go on the wall
                if self.map[self.ordinate][self.abscissa+1] != "0":
                    self.abscissa += 1  #Move one case on the right (positive axis)
                    self.pixel_x = self.abscissa * SPRITE_SIZE #Set new pixel position
        elif direction == 274: # K_LEFT
            #Check that he wont get outside the Screen
            if self.ordinate < (SPRITES_NUMBER - 1):
                #Check that he wont go on the wall
                if self.map[self.ordinate+1][self.abscissa] != "0":
                    self.ordinate += 1  #Move one case down (positive axis)
                    self.pixel_y = self.ordinate * SPRITE_SIZE #Set new pixel position
        elif direction == 276: # K_DOWN
            #Check that he wont get outside the Screen
            if self.abscissa > 0:
                #Check that he wont go on the wall
                if self.map[self.ordinate][self.abscissa-1] != "0":
                    self.abscissa -= 1  #Move one case on the left (positive axis)
                    self.pixel_x = self.abscissa * SPRITE_SIZE #Set new pixel position
        elif direction == 273: # K_UP
            #Check that he wont get outside the Screen
            if self.ordinate > 0:
                #Check that he wont go on the wall
                if self.map[self.ordinate-1][self.abscissa] != "0":
                    self.ordinate -= 1  #Move one case up (negative axis)
                    self.pixel_y = self.ordinate * SPRITE_SIZE #Set new pixel position

    @property
    def position(self):
        """
            Characters position, for image bliting
        """
        return [self.pixel_x, self.pixel_y]
