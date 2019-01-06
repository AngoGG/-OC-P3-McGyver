# OpenClassrooms Project: McGyver

## Informations
    @description    This Document will contain all the scope and analysis
                    of the OpenClassrooms "McGyver" Project.
    @author         Anthony Gomes <anthony.gomes@afnor.org>
    @version        0.1
    @date           2018-12-22
    @notes          cd D:/[OC]Formation_Python/Projet_3/[Projet]McGyver
    @note           0.1 (2018-12-22) : Document initialisation after
                    first read of the statement of the project


## Contraints
- Program should be versionned using git and hosted on GitHub
- Program should follow the PEP8 and be developped in an virtual environment using Python 3
- All program should be written in English

This will contains all the notes and specs specifications of the Game.

### Difficulties and reflexion
OpenClassrooms divised the project in 4 steps:
1. Starting Map
2. Character movement
3. Objects collecting
4. Win Conditions

The program could be written with the following classes:
- Level
- Character
- Objects

### Structure of the program
- main.py
- constants.py
- classes.py
- images/
- level (flat document containing the Labyrinth structure)

## Classes
1. **map:**
  - Level initialisation (get labyrinth file + empty structure list)
  - Window generation and display
  - Labyrinth structure definition (return a list from file)
  - Labyrinth drawing
2. **character:**
  - McGyver initialisation (position + image)
  - McGyver movement management
  - McGyver position
3. **objects:**
  - Items initialisation (images and map structure for positionning)
  - Item generation and random positionning
  - Item position

### Deroulement du programme
main:
  - pygame initialisation
  - map structure definition
  - mcgyver position initialisation
  - main_loop:
    - labyrinth display
    - get keyboard events
      - mcgyver movements
    - images refresh
    - pick up items and win conditions
