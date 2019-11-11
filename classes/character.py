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
        self.item_cells = level.get_item_position
        self.end_level = level.get_end_level

    def move(self, direction):
        """
        Movement management, check if aimed position is valid,
        if yes, assign it as new position and call check_item_on_position method
        @param string   Item found
        """
        if direction == K_RIGHT:
            new_position = [self.position[0] + 1, self.position[1]]
            if (new_position in self.empty_cells
                    or new_position == self.end_level):
                self.position = new_position
                self.check_item_on_position()
        elif direction == K_LEFT:
            new_position = [self.position[0] - 1, self.position[1]]
            if (new_position in self.empty_cells
                    or new_position == self.end_level):
                self.position = new_position
                self.check_item_on_position()
        elif direction == K_UP:
            new_position = [self.position[0], self.position[1] - 1]
            if (new_position in self.empty_cells
                    or new_position == self.end_level):
                self.position = new_position
                self.check_item_on_position()
        elif direction == K_DOWN:
            new_position = [self.position[0], self.position[1] + 1]
            if (new_position in self.empty_cells
                    or new_position == self.end_level):
                self.position = new_position
                self.check_item_on_position()

    def check_item_on_position(self):
        """
            Check if an item is on the current position, if yes, call pick_up method
        """
        if self.map[self.position[1]][self.position[0]] == "N":
            self.pick_up("NEEDLE")
        elif self.map[self.position[1]][self.position[0]] == "E":
            self.pick_up("ETHER")
        elif self.map[self.position[1]][self.position[0]] == "T":
            self.pick_up("TUBE")

    def pick_up(self, item):
        """
        Check if the item on the actual cell is already on the character
        possession, if not, add it into the list
        @param string   item    item on the actual cell
        """
        if item not in self.items:
            self.items.append(item)

    @property
    def get_character_position(self):
        """
            @return list    Return the actual charaters position
        """
        return self.position

    @property
    def get_character_items(self):
        """
            @return list    Return the items in characters position
        """
        return self.items
