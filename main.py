import pygame
from variables import *
import row
import button

pygame.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Game of Nim")

def draw(rows, buttons):
    WINDOW.fill("gray") # change background color

    for row in rows:
        for stick in row:
            pygame.draw.rect(WINDOW, "brown", stick)

    for button in buttons:
        pygame.draw.rect(WINDOW, "black", button)

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

    # initialize and create the buttons
    passButton = button.Button(rowD.Xend + 50, rowD.Ystart, STICK_HEIGHT, STICK_HEIGHT)
    helpButton = button.Button(rowD.Xend + 50, rowA.Ystart, STICK_HEIGHT, STICK_HEIGHT)
    buttons = [passButton.rect, helpButton.rect]

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
                    if pos[1] >= rowA.Ystart and pos[1] <= rowA.Yend and rowA.numSticks >= 1:
                        rowA.remove()
                if pos[0] >= rowB.Xstart and pos[0] <= rowB.Xend:
                    if pos[1] >= rowB.Ystart and pos[1] <= rowB.Yend and rowB.numSticks >= 1:
                        rowB.remove()
                if pos[0] >= rowC.Xstart and pos[0] <= rowC.Xend:
                    if pos[1] >= rowC.Ystart and pos[1] <= rowC.Yend and rowC.numSticks >= 1:
                        rowC.remove()
                if pos[0] >= rowD.Xstart and pos[0] <= rowD.Xend:
                    if pos[1] >= rowD.Ystart and pos[1] <= rowD.Yend and rowD.numSticks >= 1:
                        rowD.remove()

                if passButton.click(pos):
                    print("here")

        totalSticks = rowA.numSticks + rowB.numSticks + rowC.numSticks + rowD.numSticks
        draw(rows, buttons)

    pygame.quit()

if __name__ == "__main__":
    main()
