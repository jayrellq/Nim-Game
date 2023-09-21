import pygame
from variables import *

class Button():
    def __init__(self, X, Y, width, height):
        self.X = X
        self.Y = Y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(X, Y, width, height)

    # check if button is clicked
    def click(self, pos):
        clicked = False

        if pos[0] >= self.X and pos[0] <= self.X + self.width:
            if pos[1] >= self.Y and pos[1] <= self.Y + self.height:
                clicked = True

        return clicked
