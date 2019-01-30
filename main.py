# coding: utf-8
"""
    This will contains the main script for the McGyver Labyrinth Game
    First we gonna start to set up a basic non object code
"""
from classes.game import Game


def main():
    """
        Main Method
    """
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
