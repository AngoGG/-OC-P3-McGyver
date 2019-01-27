"""
    Will contain all the program classes
"""
import pygame
from pygame.locals import *
from classes.constants import Constants

class Display:
    """
        DocString
    """
    pygame.init()
    def __init__(self):
        self.level_structure = []
        self.height = Constants.SPRITES_NUMBER * Constants.SPRITE_SIZE
        self.width = (Constants.SPRITES_NUMBER +1) * Constants.SPRITE_SIZE

    @property
    def window_generation(self):
        """
            Window Generation, does'nt work at the moment,
            Cant get the result back to use it in show method
        """
        pygame.display.set_caption("OpenClassrooms P3 McGyver !")
        return pygame.display.set_mode((self.height, self.width))

    @staticmethod
    def display_game(location, window):
        """
            DocSring
        """
        if location == "home":
            image = pygame.image.load(Constants.HOME).convert()
            window.blit(image, (0, 0))  # displaying home screen
            pygame.display.flip()  # window refreshing
        elif location == "end":
            window.pygame.blit(Constants.END, (0, 0))  # displaying home screen
            window.blit(image, (0, 0))  # displaying home screen
            pygame.display.flip()  # window refreshing

    def display_level(self, level, character, window):
        """
            Display all the Game images while parsing the structure of the level
            Could be reduce
        """
        line_number = 0
        for line in level.get_map_structure:
            case_number = 0
            for sprite in line:
                x = case_number * Constants.SPRITE_SIZE
                y = line_number * Constants.SPRITE_SIZE
                if sprite == "0":
                    window.blit(pygame.image.load(Constants.WALL).convert(),
                                (x, y))
                elif sprite == "N":
                    window.blit(pygame.image.load(Constants.FLOOR).convert(),
                                (x, y))
                    if "NEEDLE" not in character.character_items:
                        window.blit(pygame.image.load(Constants.ITEMS[0]['image'])
                                    .convert(), (x, y))
                    else:
                        window.blit(pygame.image.load(Constants.ITEMS[0]['image'])
                                    .convert(), (0, 450))
                elif sprite == "E":
                    window.blit(pygame.image.load(Constants.FLOOR).convert(),
                                (x, y))
                    if "ETHER" not in character.character_items:
                        window.blit(pygame.image.load(Constants.ITEMS[1]['image'])
                                    .convert(), (x, y))
                    else:
                        window.blit(pygame.image.load(Constants.ITEMS[1]['image'])
                                    .convert(), (30, 450))
                elif sprite == "T":
                    window.blit(pygame.image.load(Constants.FLOOR).convert(),
                                (x, y))
                    if "TUBE" not in character.character_items:
                        window.blit(pygame.image.load(Constants.ITEMS[2]['image'])
                                    .convert(), (x, y))
                    else:
                        window.blit(pygame.image.load(Constants.ITEMS[2]['image'])
                                    .convert(), (60, 450))
                elif sprite in ("C", "1"):
                    window.blit(pygame.image.load(Constants.FLOOR).convert(),
                                (x, y))
                elif sprite == "G":
                    window.blit(pygame.image.load(Constants.FLOOR).convert(),
                                (x, y))
                    window.blit(pygame.image.load(Constants.GUARD).convert(),
                                (x, y))
                case_number += 1
            line_number += 1

            #Ajout Image Character
            window.blit(pygame.image.load(Constants.CHARACTER).convert(),
                        (character.character_position[0] * Constants.SPRITE_SIZE,
                         character.character_position[1] * Constants.SPRITE_SIZE))

            #Gestion des items ramassés

            pygame.display.flip()  # window refreshing
