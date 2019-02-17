"""
@desc    Only contain Class Character, see the description below
"""
import pygame
from pygame.locals import *


class Character:
    """
    Character management:
    Movement and item picking up
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
        self.end_level = level.get_end_level

    def add_item(self, item):
        """
        Update Character item List when an item is found
        @param string   Item found
        """
        self.items.append(item)

    def move(self, direction):
        """
        Movement management, check if aimed position is valid,
        if yes, assign it as new position
        If aimed position is an item cell, call pick_up method
        @param string   Item found
        """
        if direction == K_RIGHT:
            new_position = [self.position[0] + 1, self.position[1]]
            if (new_position in self.empty_cells
                    or new_position == self.end_level):
                self.position = new_position
                if self.map[new_position[1]][new_position[0]] == "N":
                    self.pick_up("NEEDLE")
                elif self.map[new_position[1]][new_position[0]] == "E":
                    self.pick_up("ETHER")
                elif self.map[new_position[1]][new_position[0]] == "T":
                    self.pick_up("TUBE")
        elif direction == K_LEFT:
            new_position = [self.position[0] - 1, self.position[1]]
            if (new_position in self.empty_cells
                    or new_position == self.end_level):
                self.position = new_position
                if self.map[new_position[1]][new_position[0]] == "N":
                    self.pick_up("NEEDLE")
                elif self.map[new_position[1]][new_position[0]] == "E":
                    self.pick_up("ETHER")
                elif self.map[new_position[1]][new_position[0]] == "T":
                    self.pick_up("TUBE")
        elif direction == K_UP:
            new_position = [self.position[0], self.position[1] - 1]
            if (new_position in self.empty_cells
                    or new_position == self.end_level):
                self.position = new_position
                if self.map[new_position[1]][new_position[0]] == "N":
                    self.pick_up("NEEDLE")
                elif self.map[new_position[1]][new_position[0]] == "E":
                    self.pick_up("ETHER")
                elif self.map[new_position[1]][new_position[0]] == "T":
                    self.pick_up("TUBE")
        elif direction == K_DOWN:
            new_position = [self.position[0], self.position[1] + 1]
            if (new_position in self.empty_cells
                    or new_position == self.end_level):
                self.position = new_position
                if self.map[new_position[1]][new_position[0]] == "N":
                    self.pick_up("NEEDLE")
                elif self.map[new_position[1]][new_position[0]] == "E":
                    self.pick_up("ETHER")
                elif self.map[new_position[1]][new_position[0]] == "T":
                    self.pick_up("TUBE")

    def pick_up(self, item):
        """
        Check if the item on the actual cell is already on the character
        possession
        @param string   item    item on the actual cell
        """
        if item not in self.items:
            self.items.append(item)

    @property
    def character_position(self):
        """
            @return list    Return the actual charaters position
        """
        return self.position

    @property
    def character_items(self):
        """
            @return list    Return the items in characters position
        """
        return self.items
