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
        home = 1
        play = 0
        end = 0
        while home:
            pygame.time.Clock().tick(30)
            game.display_game("home", window)
            for event in pygame.event.get():
                if event.type == QUIT:
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
            win = 0
            lose = 0
            end = 0
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    play = 0
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        play = 0
                    else:
                        character.move(event.key)
            if character.character_position == level.get_end_level:
                if len(character.items) == 3:
                    play = 0
                    win = 1
                    end = 1
                else:
                    play = 0
                    lose = 1
                    end = 1
            else:
                game.display_level(level, character, window)
        while end:
            if win == 1:
                game.display_game("win", window)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        end = 0
            elif lose == 1:
                game.display_game("lose", window)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        end = 0
