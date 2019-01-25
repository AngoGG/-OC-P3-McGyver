"""
    Will contain all the program classes
"""
import pygame
from pygame.locals import *
from classes.constants import Constants
from classes.level import Newlevel

class Display:
    """
        DocString
    """
    pygame.init()
    def __init__(self):
        self.level_structure = []
        self.height = Constants.SPRITES_NUMBER * Constants.SPRITE_SIZE
        self.width = Constants.SPRITES_NUMBER * Constants.SPRITE_SIZE

    def window_generation(self):
        """
            Window Generation, does'nt work at the moment,
            Cant get the result back to use it in show method
        """
        return pygame.display.set_mode((self.height, self.width))

    @classmethod
    def display_game(cls, location, window):
        """
            DocSring
        """
        if location == "home":
            image = pygame.image.load("images/mcgyver_home.png").convert()
            window.blit(image, (0, 0))  # displaying home screen
            pygame.display.flip()  # window refreshing
        elif location == "end":
            window.pygame.blit(Constants.END, (0, 0))  # displaying home screen

    def display_level(self, window):
        """
            DocSring
        """
        level = Newlevel()
        self.level_structure = level.get_structure()
        character = level.character_position()
        character_pixel_x = character[0]
        character_pixel_y = character[1]
        line_number = 0
        for line in self.level_structure:
            case_number = 0
            for sprite in line:
                abscissa = case_number * Constants.SPRITE_SIZE
                ordinate = line_number * Constants.SPRITE_SIZE
                if sprite == "0":
                    window.blit(pygame.image.load(Constants.WALL).convert(),
                                (abscissa, ordinate))
                elif sprite == "N":
                    window.blit(pygame.image.load(Constants.FLOOR).convert(),
                                (abscissa, ordinate))
                    window.blit(pygame.image.load(Constants.ITEMS[0]['image'])
                                .convert(), (abscissa, ordinate))
                elif sprite == "E":
                    window.blit(pygame.image.load(Constants.FLOOR).convert(),
                                (abscissa, ordinate))
                    window.blit(pygame.image.load(Constants.ITEMS[1]['image'])
                                .convert(), (abscissa, ordinate))
                elif sprite == "T":
                    window.blit(pygame.image.load(Constants.FLOOR).convert(),
                                (abscissa, ordinate))
                    window.blit(pygame.image.load(Constants.ITEMS[2]['image'])
                                .convert(), (abscissa, ordinate))
                elif sprite in ("C", "1"):
                    window.blit(pygame.image.load(Constants.FLOOR).convert(),
                                (abscissa, ordinate))
                elif sprite == "G":
                    window.blit(pygame.image.load(Constants.FLOOR).convert(),
                                (abscissa, ordinate))
                    window.blit(pygame.image.load(Constants.GUARD).convert(),
                                (abscissa, ordinate))
                case_number += 1
            line_number += 1
            window.blit(pygame.image.load(Constants.CHARACTER).convert(),
                        (character_pixel_x, character_pixel_y))
        pygame.display.flip()  # window refreshing
