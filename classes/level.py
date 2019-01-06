"""
    Will contain all the program classes
"""
import pygame
from pygame.locals import *
from constants import SPRITE_SIZE, FILE, WALL, FLOOR, GUARD

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
