# coding: utf-8
"""
@desc    OpenClassrooms third Projet code
@author  Anthony Gomes <anthony.gomes@afnor.org>
@version 2.0.0
@date    2019-01-30
@note    2.0.0 (2019-01-30) : Refactored Final, Version, comments to add
"""
from classes.game import Game


def main():
    """
    Main Method, just launches the Game class who drive the whole programm
    """
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
