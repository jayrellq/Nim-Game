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
    rowA.createRow()
    rowB.createRow()
    rowC.createRow()
    rowD.createRow()
    rows = [rowA.arr, rowB.arr, rowC.arr, rowD.arr]

    # initialize and create the buttons
    AButton = button.Button(rowD.Xstart - 100, rowA.Ystart, STICK_HEIGHT, STICK_HEIGHT)
    BButton = button.Button(rowD.Xstart - 100, rowB.Ystart, STICK_HEIGHT, STICK_HEIGHT)
    CButton = button.Button(rowD.Xstart - 100, rowC.Ystart, STICK_HEIGHT, STICK_HEIGHT)
    DButton = button.Button(rowD.Xstart - 100, rowD.Ystart, STICK_HEIGHT, STICK_HEIGHT)
    passButton = button.Button(rowD.Xend + 50, rowD.Ystart, STICK_HEIGHT, STICK_HEIGHT)
    helpButton = button.Button(rowD.Xend + 50, rowA.Ystart, STICK_HEIGHT, STICK_HEIGHT)
    buttons = [AButton.rect, BButton.rect, CButton.rect, DButton.rect, passButton.rect, helpButton.rect]

    while run:
        for event in pygame.event.get():
            # check if window is closed
            if event.type == pygame.QUIT:
                run = False
                break
            # check for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                if AButton.click(pos) and rowA.numSticks >= 1:
                    rowA.removeStick()
                if BButton.click(pos) and rowB.numSticks >= 1:
                    rowB.removeStick()
                if CButton.click(pos) and rowC.numSticks >= 1:
                    rowC.removeStick()
                if DButton.click(pos) and rowD.numSticks >= 1:
                    rowD.removeStick()

                if passButton.click(pos):
                    print("here")

        totalSticks = rowA.numSticks + rowB.numSticks + rowC.numSticks + rowD.numSticks
        draw(rows, buttons)

    pygame.quit()

if __name__ == "__main__":
    main()
