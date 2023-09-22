import pygame
from variables import *

class Button():
    def __init__(self, X, Y, width, height, font, text):
        self.X = X
        self.Y = Y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(X, Y, width, height)

        self.text = font.render(text, 1, "white")
        self.textRect = self.text.get_rect(center=(X + width/2, Y + height/2))

    # check if button is clicked
    def click(self):
        pos = pygame.mouse.get_pos()
        clicked = False

        if pos[0] >= self.X and pos[0] <= self.X + self.width:
            if pos[1] >= self.Y and pos[1] <= self.Y + self.height:
                clicked = True

        return clicked
