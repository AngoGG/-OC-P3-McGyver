"""
@desc    Only contain Class Display, see the description below
"""
import pygame
from pygame.locals import *
from classes.constants import Constants


class Display:
    """
    Pygame Display management
    """
    pygame.init()

    def __init__(self):
        self.level_structure = []
        self.height = Constants.SPRITES_NUMBER * Constants.SPRITE_SIZE
        self.width = (Constants.SPRITES_NUMBER + 1) * Constants.SPRITE_SIZE

    @property
    def window_generation(self):
        """
        Window Generation
        """
        pygame.display.set_caption("OpenClassrooms P3 McGyver !")
        return pygame.display.set_mode((self.height, self.width))

    @staticmethod
    def display_image(image, position, window):
        """
        Display game while moving on the board
        @param  string  image     Path to the image to display
        @param  tuple   position  Tuple containing abscissa and ordinate to display the image
        """
        window.blit(pygame.image.load(image).convert(),
                                position)

    def display_game(self, location, window):
        """
        Start/End display Management according to the state of the game
        """
        if location == "home":
            self.display_image(Constants.HOME, (0, 0), window)
            pygame.display.flip()  # window refreshing
        elif location == "win":
            self.display_image(Constants.WIN, (0, 0), window)
            pygame.display.flip()  # window refreshing
        elif location == "lose":
            self.display_image(Constants.LOSE, (0, 0), window)
            pygame.display.flip()  # window refreshing

    
    def display_level(self, level, character, window):
        """
        Display all the Game images from the structure level
            and character position
        @param  object  level       Contain level object
        @param  object  characters  Contain character object
        @param  object  window      Contain the pygame window
        """
        line_number = 0
        for line in level.get_map_structure:
            case_number = 0
            for sprite in line:
                x = case_number * Constants.SPRITE_SIZE
                y = line_number * Constants.SPRITE_SIZE
                if sprite == "0":
                    self.display_image(Constants.WALL, (x, y), window)
                elif sprite == "N":
                    self.display_image(Constants.FLOOR, (x, y), window)
                    if "NEEDLE" not in character.get_character_items:
                        self.display_image(Constants.ITEMS[0]['image'], (x, y), window)
                    else:
                        self.display_image(Constants.ITEMS[0]['image'], (0, 450), window)
                elif sprite == "E":
                    self.display_image(Constants.FLOOR, (x, y), window)
                    if "ETHER" not in character.get_character_items:
                        self.display_image(Constants.ITEMS[1]['image'], (x, y), window)
                    else:
                        self.display_image(Constants.ITEMS[1]['image'], (30, 450), window)
                elif sprite == "T":
                    self.display_image(Constants.FLOOR, (x, y), window)
                    if "TUBE" not in character.get_character_items:
                        self.display_image(Constants.ITEMS[2]['image'], (x, y), window)
                    else:
                        self.display_image(Constants.ITEMS[2]['image'], (60, 450), window)
                elif sprite in ("C", "1"):
                   self.display_image(Constants.FLOOR, (x, y), window)
                elif sprite == "G":
                    self.display_image(Constants.FLOOR, (x, y), window)
                    self.display_image(Constants.GUARD, (x, y), window)
                case_number += 1
            line_number += 1
            self.display_image(Constants.CHARACTER, (character.get_character_position[0]
                         * Constants.SPRITE_SIZE,
                         character.get_character_position[1]
                         * Constants.SPRITE_SIZE), window)
            pygame.display.flip()

    
