"""
    Will contain all the program classes
"""
import pygame
from pygame.locals import *


class Character:
    """
        Main Character class
        Generation and motion management
    """
    def __init__(self, level):
        """
            Actual characters position
        """
        self.items = []
        self.map = level.get_map_structure
        self.position = level.get_character_start
        self.empty_cells = level.get_empty_cells
        self.item_cells = level.item_position

    def add_item(self, item):
        """
            Update item List when character find one
        """
        self.items.append(item)

    def move(self, direction):
        """
            DocSring
        """
        if direction == K_RIGHT:
            new_position = [self.position[0] + 1, self.position[1]]
            if new_position in self.empty_cells:
                self.position = new_position
                if self.map[new_position[1]][new_position[0]] == "N":
                    Character.pick_up(self, "NEEDLE")
                elif self.map[new_position[1]][new_position[0]] == "E":
                    Character.pick_up(self, "ETHER")
                elif self.map[new_position[1]][new_position[0]] == "T":
                    Character.pick_up(self, "TUBE")
        elif direction == K_LEFT:
            new_position = [self.position[0] - 1, self.position[1]]
            if new_position in self.empty_cells:
                self.position = new_position
                if self.map[new_position[1]][new_position[0]] == "N":
                    Character.pick_up(self, "NEEDLE")
                elif self.map[new_position[1]][new_position[0]] == "E":
                    Character.pick_up(self, "ETHER")
                elif self.map[new_position[1]][new_position[0]] == "T":
                    Character.pick_up(self, "TUBE")
        elif direction == K_UP:
            new_position = [self.position[0], self.position[1] - 1]
            if new_position in self.empty_cells:
                self.position = new_position
                if self.map[new_position[1]][new_position[0]] == "N":
                    Character.pick_up(self, "NEEDLE")
                elif self.map[new_position[1]][new_position[0]] == "E":
                    Character.pick_up(self, "ETHER")
                elif self.map[new_position[1]][new_position[0]] == "T":
                    Character.pick_up(self, "TUBE")
        elif direction == K_DOWN:
            new_position = [self.position[0], self.position[1] + 1]
            if new_position in self.empty_cells:
                self.position = new_position
                if self.map[new_position[1]][new_position[0]] == "N":
                    Character.pick_up(self, "NEEDLE")
                elif self.map[new_position[1]][new_position[0]] == "E":
                    Character.pick_up(self, "ETHER")
                elif self.map[new_position[1]][new_position[0]] == "T":
                    Character.pick_up(self, "TUBE")

    def pick_up(self, item):
        """
            DocSring
        """
        if item not in self.items:
            self.items.append(item)

    @property
    def character_position(self):
        """
            DocSring
        """
        return self.position

    @property
    def character_items(self):
        """
            DocSring
        """
        return self.items
