"""
    Will contain all the program classes
"""
from random import randint
import pygame
from pygame.locals import *
from constants import *

class Level:
    """
        Generation of the Labyrinth Design from a flat file
    """
    def __init__(self):
        self.file = FILE
        self.level_structure = []

    @classmethod
    def window_generation(cls):
        """
            Window Generation, does'nt work at the moment,
            Cant get the result back to use it in show method
        """
        return pygame.display.set_mode((450, 480))

    def get_labyrinth_structure(self):
        """
            Labyrinth data recuperation from file
        """
        with open(self.file, "r") as fichier:
            level_structure = []
            for line in fichier:
                line_level = []
                for sprite in line:
                    if sprite != "\n":
                        line_level.append(sprite)
                level_structure.append(line_level)
            self.level_structure = level_structure
            return self.level_structure

    def set_labyrinth(self, window):
        """
            Generation of the map using map_data
                - Add image to each part of the map, basically wall, floor & guardian for the finish
                - Starting from top left with line & sprite = 0, then go for line after line filling
        """
        wall = pygame.image.load(WALL).convert()
        floor = pygame.image.load(FLOOR).convert()
        guard = pygame.image.load(GUARD).convert_alpha()

        line_number = 0
        for line in self.level_structure:
            case_number = 0
            for sprite in line:
                abscissa = case_number * SPRITE_SIZE
                ordinate = line_number * SPRITE_SIZE
                if sprite == "0":
                    window.blit(wall, (abscissa, ordinate))
                elif sprite in ("C", "I", "1"):
                    window.blit(floor, (abscissa, ordinate))
                elif sprite == "G":
                    window.blit(floor, (abscissa, ordinate))
                    window.blit(guard, (abscissa, ordinate))
                case_number += 1
            line_number += 1

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

class Item:
    """
        Item class, basically
    """
    def __init__(self, map_structure, item):
        """
            Init
        """
        self.image = pygame.image.load(item).convert_alpha()
        self.syringe_image = pygame.image.load(SYRINGE).convert_alpha()
        self.map = map_structure
        self.pixel_x = 0
        self.pixel_y = 0
        self.got_item = False


    def item_position(self, item):
        """
            Hey
        """
        if item == "needle":
            ok_position = None
            while ok_position is None:
                rand_ligne = randint(0, 14)
                rand_case = randint(0, 13)
                if self.map[rand_ligne][rand_case] == "1":
                    self.pixel_x = rand_case * SPRITE_SIZE
                    self.pixel_y = rand_ligne * SPRITE_SIZE
                    ok_position = True
                    # We replace the sprite to ensure we cannot get 2 item on it
                    self.map[rand_ligne][rand_case] = "I"
        elif item == "ether":
            ok_position = None
            while ok_position is None:
                rand_ligne = randint(0, 14)
                rand_case = randint(0, 13)
                if self.map[rand_ligne][rand_case] == "1":
                    self.pixel_x = rand_case * SPRITE_SIZE
                    self.pixel_y = rand_ligne * SPRITE_SIZE
                    ok_position = True
                    # We replace the sprite to ensure we cannot get 2 item on it
                    self.map[rand_ligne][rand_case] = "I"
        elif item == "tube":
            ok_position = None
            while ok_position is None:
                rand_ligne = randint(0, 14)
                rand_case = randint(0, 13)
                if self.map[rand_ligne][rand_case] == "1":
                    self.pixel_x = rand_case * SPRITE_SIZE
                    self.pixel_y = rand_ligne * SPRITE_SIZE
                    ok_position = True
                    # We replace the sprite to ensure we cannot get 2 item on it
                    self.map[rand_ligne][rand_case] = "I"

    def display(self, window, item, item_number):
        """
            Display management of items
        """
        if self.got_item is False:
            window.blit(self.image, (self.position))
        elif item_number == 3:
            window.blit(self.syringe_image, [40, 450])
        elif item == "needle":
            window.blit(self.image, [0, 450])
        elif item == "ether":
            window.blit(self.image, [40, 450])
        elif item == "tube":
            window.blit(self.image, [80, 450])

    @property
    def position(self):
        """
            Characters position, for image bliting
        """
        return [self.pixel_x, self.pixel_y]
