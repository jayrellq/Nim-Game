import pygame
from variables import *
import row

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Game of Nim")

def draw(rows):
    WINDOW.fill("gray") # change background color

    for row in rows:
        for stick in row:
            pygame.draw.rect(WINDOW, "brown", stick)

    pygame.display.update() # refresh display to update any drawings

def main():
    run = True

    # initialize and create the rows
    rowA = row.Row(1, (WIDTH-STICK_WIDTH)/2, 75)
    rowB = row.Row(3, (WIDTH-STICK_WIDTH)/2, 75)
    rowC = row.Row(5, (WIDTH-STICK_WIDTH)/2, 75)
    rowD = row.Row(7, (WIDTH-STICK_WIDTH)/2, 75)
    rowA.create()
    rowB.create()
    rowC.create()
    rowD.create()
    rows = [rowA.arr, rowB.arr, rowC.arr, rowD.arr]
    totalSticks = rowA.numSticks + rowB.numSticks + rowC.numSticks + rowD.numSticks

    while run:
        for event in pygame.event.get():
            # check if window is closed
            if event.type == pygame.QUIT:
                run = False
                break
            # check for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                if pos[0] >= rowA.Xstart and pos[0] <= rowA.Xend:
                    if pos[1] >= rowA.Ystart and pos[1] <= rowA.Yend and len(rowA.arr) >= 1:
                        rowA.arr.pop(0)
                        totalSticks -= 1
                if pos[0] >= rowB.Xstart and pos[0] <= rowB.Xend:
                    if pos[1] >= rowB.Ystart and pos[1] <= rowB.Yend and len(rowB.arr) >= 1:
                        rowB.arr.pop(0)
                        totalSticks -= 1
                if pos[0] >= rowC.Xstart and pos[0] <= rowC.Xend:
                    if pos[1] >= rowC.Ystart and pos[1] <= rowC.Yend and len(rowC.arr) >= 1:
                        rowC.arr.pop(0)
                        totalSticks -= 1
                if pos[0] >= rowD.Xstart and pos[0] <= rowD.Xend:
                    if pos[1] >= rowD.Ystart and pos[1] <= rowD.Yend and len(rowD.arr) >= 1:
                        rowD.arr.pop(0)
                        totalSticks -= 1

        draw(rows)

    pygame.quit()

if __name__ == "__main__":
    main()
