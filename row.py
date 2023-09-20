import pygame
from variables import *

class Row():
    def __init__(self, numSticks, X, Y):
        self.arr = []
        self.numSticks = numSticks
        self.Xstart = X - (((self.numSticks-1)/2) * STICK_WIDTH_SPACE)
        self.Xend = self.Xstart
        self.Ystart = Y + (((numSticks-1)/2) * STICK_HEIGHT_SPACE)
        self.Yend = self.Ystart

    def create(self):
        for i in range(self.numSticks):
            stick = pygame.Rect(self.Xend, self.Ystart, STICK_WIDTH, STICK_HEIGHT)
            self.arr.append(stick)
            self.Xend += STICK_WIDTH_SPACE

        self.Xend = self.Xend - STICK_WIDTH_SPACE + STICK_WIDTH # remove the added spacing at the end and add stick width
        self.Yend = self.Yend + STICK_HEIGHT
