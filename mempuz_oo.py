# refactor of Al Sweigart's "Memory Puzzle" (http://inventwithpython.com/pygame/chapter3.html)

# import required modules and the game data
import pygame
import mempuz_oo_data

# define the classes

class Shape:
    """
    The main Shape class for the program, storing the shape, color, and revealed state of the game board objects.
    """
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.reveal = False # initialize the boxes to not be revealed

    def flip(self):
        """
        Flips the reveal status of the Shape object from True to False, and False to True, when called.
        """
        if self.reveal == False:
            self.reveal = True
        else:
            self.reveal = False

class Board:
    """
    the game board object, which holds the color of the playfield, the dimensions of the board, and
    """
