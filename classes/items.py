"""
    Will contain all the program classes
"""
from random import randint
import pygame
from pygame.locals import *
from constants import SPRITE_SIZE, SYRINGE

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
