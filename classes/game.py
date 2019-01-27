# coding: utf-8
"""
    DocString
"""
import pygame
from pygame.locals import *
from classes.display import Display
from classes.level import Level
from classes.character import Character

class Game:
    """
        This class will drive the entire programm
    """
    @staticmethod
    def play():
        """
            DocSring
        """
        game = Display()
        window = game.window_generation
        home = 1
        while home:
            pygame.time.Clock().tick(30)
            game.display_game("home", window)
            for event in pygame.event.get():
                if event.type == QUIT: # QUIT
                    home = 0
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        home = 0
                        level = Level()
                        level.get_structure()
                        character = Character(level)
                        game.display_level(level, character, window)
                        play = 1
        while play:
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == QUIT: # QUIT
                    play = 0
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        play = 0
                    else:
                        character.move(event.key)
                        if character.character_position == level.get_end_level:
                            if len(character.items) == 3:
                                print('WIN')
                            else:
                                print('LOSE')
                        game.display_level(level, character, window)
