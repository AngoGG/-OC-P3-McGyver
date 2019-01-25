"""
    Will contain all the program classes
"""
import pygame
from pygame.locals import *
from classes.constants import Constants

class NewCharacter():
    """
        Main Character class
        Generation and motion management
    """
    def __init__(self):
        """
            Actual characters position
        """
        self.items = []
        self.position = []

    def add_item(self, item):
        """
            Update item List when character find one
        """
        self.items.append(item)
        return self.items

    def move(self, direction):
        """
            Make the character move
        """
        if direction == K_RIGHT:
            #Check that he wont get outside the Screen
            if self.abscissa < (constants.SPRITES_NUMBER - 1):
                #Check that he wont go on the wall, if not move and set position
                if self.map[self.ordinate][self.abscissa+1] != "0":
                    self.abscissa += 1
                    self.pixel_x = self.abscissa * Constants.SPRITE_SIZE
        elif direction == K_LEFT:
            #Check that he wont get outside the Screen
            if self.abscissa > 0:
                #Check that he wont go on the wall, if not move and set position
                if self.map[self.ordinate][self.abscissa-1] != "0":
                    self.abscissa -= 1
                    self.pixel_x = self.abscissa * Constants.SPRITE_SIZE
        elif direction == K_DOWN:
            #Check that he wont get outside the Screen
            if self.ordinate < (constants.SPRITES_NUMBER - 1):
                #Check that he wont go on the wall, if not move and set position
                if self.map[self.ordinate+1][self.abscissa] != "0":
                    self.ordinate += 1
                    self.pixel_y = self.ordinate * Constants.SPRITE_SIZE

        elif direction == K_UP:
            #Check that he wont get outside the Screen
            if self.ordinate > 0:
                #Check that he wont go on the wall, if not move and set position
                if self.map[self.ordinate-1][self.abscissa] != "0":
                    self.ordinate -= 1
                    self.pixel_y = self.ordinate * Constants.SPRITE_SIZE



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
        self.image = pygame.image.load(Constants.MCGYVER).convert_alpha()

    def move(self, direction):
        """
            Make the character move
        """
        if direction == K_RIGHT:
            #Check that he wont get outside the Screen
            if self.abscissa < (constants.SPRITES_NUMBER - 1):
                #Check that he wont go on the wall, if not move and set position
                if self.map[self.ordinate][self.abscissa+1] != "0":
                    self.abscissa += 1
                    self.pixel_x = self.abscissa * Constants.SPRITE_SIZE
        elif direction == K_LEFT:
            #Check that he wont get outside the Screen
            if self.abscissa > 0:
                #Check that he wont go on the wall, if not move and set position
                if self.map[self.ordinate][self.abscissa-1] != "0":
                    self.abscissa -= 1
                    self.pixel_x = self.abscissa * Constants.SPRITE_SIZE
        elif direction == K_DOWN:
            #Check that he wont get outside the Screen
            if self.ordinate < (constants.SPRITES_NUMBER - 1):
                #Check that he wont go on the wall, if not move and set position
                if self.map[self.ordinate+1][self.abscissa] != "0":
                    self.ordinate += 1
                    self.pixel_y = self.ordinate * Constants.SPRITE_SIZE

        elif direction == K_UP:
            #Check that he wont get outside the Screen
            if self.ordinate > 0:
                #Check that he wont go on the wall, if not move and set position
                if self.map[self.ordinate-1][self.abscissa] != "0":
                    self.ordinate -= 1
                    self.pixel_y = self.ordinate * Constants.SPRITE_SIZE

    @property
    def position(self):
        """
            Characters position, for image bliting
        """
        return [self.pixel_x, self.pixel_y]
