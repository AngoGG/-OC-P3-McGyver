"""
    Will contain all the program classes
"""
import random
from classes.constants import Constants


class Level:
    """
        Parsing Input Labyrinth
        Level Structure Generation
            Wall, Moving Zone, Guard, Character
            Return list of empty zone for items Generation
        Item position Generation
        Character starting position
    """

    def __init__(self):
        self.file = Constants.FILE
        self.structure = []
        self.empty_cells = []
        self.character_start = []
        self.items_cells = []
        self.end_level = []

    def get_structure(self):
        """
            Parsing File, return Structure List
            Update empty_cell
        """
        with open(self.file, "r") as fichier:
            structure = []
            empty_cell = []
            end_level = []
            y = 0
            for line in fichier:
                x = 0
                line_level = []
                for sprite in line:
                    if sprite != "\n":
                        if sprite == "0":
                            line_level.append(sprite)
                        elif sprite == "C":
                            character_start = [x, y]
                            line_level.append(sprite)
                        elif sprite in ("1", "G"):
                            empty_cell.append([x, y])
                            line_level.append(sprite)
                            if sprite == "G":
                                end_level = [x, y]
                    x += 1
                structure.append(line_level)
                y += 1
            # Care, level structure should be read as [y, x]
            self.structure = structure
            self.empty_cells = empty_cell
            self.character_start = character_start
            self.end_level = end_level
            Level.put_item_on_map(self)
            return self.structure

    def put_item_on_map(self):
        """
            Place each item on an empty cell
        """
        items_cells = random.sample(self.empty_cells, 3)
        self.items_cells = items_cells
        for i, item in enumerate(Constants.ITEMS):
            self.structure[int(items_cells[i]
                               [1])][int(items_cells[i][0])] = item['map']

    @property
    def item_position(self):
        """
            On ne sait pas si on va avoir besoin de ça, à voir
        """
        return self.items_cells

    @property
    def get_character_start(self):
        """
            DocString
        """
        return self.character_start

    @property
    def get_map_structure(self):
        """
            DocString
        """
        return self.structure

    @property
    def get_empty_cells(self):
        """
            DocString
        """
        return self.empty_cells

    @property
    def get_end_level(self):
        """
            DocString
        """
        return self.end_level
