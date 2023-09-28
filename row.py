import pygame
from variables import *

# only for rows with odd number of sticks
class Row():
    def __init__(self, numSticks, Xmid, Ytop):
        self.arr = []
        self.numSticks = numSticks
        self.Xstart = Xmid - (((numSticks-1)/2) * STICK_WIDTH_SPACE)
        self.Xend = self.Xstart + (numSticks-1)*STICK_WIDTH_SPACE + STICK_WIDTH
        self.Ystart = Ytop + (((numSticks-1)/2) * STICK_HEIGHT_SPACE)
        self.Yend = self.Ystart + STICK_HEIGHT

    # create the sticks for the row
    def createRow(self):
        tempXstart = self.Xstart

        for i in range(self.numSticks):
            stick = pygame.Rect(tempXstart, self.Ystart, STICK_WIDTH, STICK_HEIGHT)
            self.arr.append(stick)
            tempXstart += STICK_WIDTH_SPACE

    # remove a stick from the row
    def removeStick(self):
        self.arr.pop(0)
        self.numSticks -= 1
