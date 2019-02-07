# coding: utf-8
"""
@desc    Only contain Class Game, see the description below
"""
import pygame
from pygame.locals import *
from classes.level import Level
from classes.character import Character
from classes.display import Display


class Game:
    """
    Main Class of the programm, only contains def function
    """

    @staticmethod
    def play():
        """
        Drives the whole things:
        - Game management (Home, Game, End)
        - Launch the needed classes to play the game
            (level/character/display)
        - Pygame.event capture
        """
        game = Display()
        window = game.window_generation
        home = True
        play = False
        while home:
            pygame.time.Clock().tick(30)
            game.display_game("home", window)
            for event in pygame.event.get():
                if event.type == QUIT:
                    home = False
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        home = False
                        level = Level()
                        level.get_structure()
                        character = Character(level)
                        game.display_level(level, character, window)
                        play = True
        while play:
            win = lose = end = False
            #lose = False
            #end = False
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    play = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        play = False
                    else:
                        character.move(event.key)
            if character.character_position == level.get_end_level:
                if len(character.items) == 3:
                    play = False
                    end = win = True
                    #end = True
                else:
                    play = False
                    end = lose = True
                    #end = True
            else:
                game.display_level(level, character, window)
        while end:
            if win is True:
                game.display_game("win", window)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        end = False
            elif lose is True:
                game.display_game("lose", window)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        end = False
