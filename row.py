import pygame
from variables import *

class Row():
    def __init__(self, numSticks, Xmid, Ytop):
        self.arr = []
        self.numSticks = numSticks
        self.Xstart = Xmid - (((numSticks-1)/2) * STICK_WIDTH_SPACE)
        self.Xend = self.Xstart
        self.Ystart = Ytop + (((numSticks-1)/2) * STICK_HEIGHT_SPACE)
        self.Yend = self.Ystart

    # create the sticks for the row
    def createRow(self):
        for i in range(self.numSticks):
            stick = pygame.Rect(self.Xend, self.Ystart, STICK_WIDTH, STICK_HEIGHT)
            self.arr.append(stick)
            self.Xend += STICK_WIDTH_SPACE

        self.Xend = self.Xend - STICK_WIDTH_SPACE + STICK_WIDTH # remove added spacing at end and add stick width
        self.Yend = self.Yend + STICK_HEIGHT

    # remove a stick from the row
    def removeStick(self):
        self.arr.pop(0)
        self.numSticks -= 1
