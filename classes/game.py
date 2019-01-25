# coding: utf-8
"""
    DocString
"""
import pygame
from pygame.locals import *
from classes.display import Display
from classes.level import Newlevel
from classes.character import NewCharacter

class Game:
    """
        DocSring
    """

    def play(self):
        """
            DocSring
        """
        game = Display()
        window = game.window_generation()
        home = 1
        while home:
            game.display_game("home", window)
            for event in pygame.event.get():
                if event.type == QUIT: # QUIT
                    home = 0
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        home = 0
                        game.display_level(window)
                        character = NewCharacter()
                        play = 1
        while play:
            for event in pygame.event.get():
                if event.type == QUIT: # QUIT
                    play = 0
                else:
                    character.move(event.key)
