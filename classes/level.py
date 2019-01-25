"""
    Will contain all the program classes
"""
import random
from classes.constants import Constants
from classes.character import NewCharacter


class Newlevel:
    """
        Parsing Input Labyrinth
        Level Structure Generation
            Wall, Moving Zone, Guard, Character
            Return list of empty zone for items Generation
        Item position Generation
        Retour Structure finale
    """

    def __init__(self):
        self.file = Constants.FILE
        self.level_structure = []
        self.empty_cells = []
        self.character_start = []

    def get_structure(self):
        """
            Parsing File, return Structure List
            Update empty_cell
        """
        with open(self.file, "r") as fichier:
            level_structure = []
            empty_cell = []
            abscissa = 0
            ordonate = 0
            for line in fichier:
                line_level = []
                for sprite in line:
                    if sprite != "\n":
                        if sprite in ("0", "G"):
                            line_level.append(sprite)
                            abscissa += 1
                        elif sprite == "C":
                            character_start = [abscissa, ordonate]
                            line_level.append(sprite)
                            abscissa += 1
                        elif sprite == "1":
                            empty_cell.append([abscissa, ordonate])
                            line_level.append(sprite)
                            abscissa += 1
                level_structure.append(line_level)
                ordonate += 1
                abscissa = 0
            self.level_structure = level_structure
            self.empty_cells = empty_cell
            self.character_start = character_start
            Newlevel.put_item_on_map(self)
            return self.level_structure

    def put_item_on_map(self):
        """
            Place each item on an empty cell
        """
        for item in Constants.ITEMS:
            item_cell = random.choice(self.empty_cells)
            self.empty_cells.remove(item_cell)
            self.level_structure[int(item_cell[0])][int(item_cell[1])] = item["map"]

    def character_move(self):
        """
            DocString
        """

    def character_position(self):
        """
            DocString
        """
        return self.character_start
