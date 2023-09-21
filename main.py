import pygame
from variables import *
import row
import button

pygame.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Game of Nim")

FONT = pygame.font.SysFont("timesnewroman", 30)

def draw(rows, buttons, player):
    WINDOW.fill("gray") # change background color

    # display whose turn is it
    turnPlayer = FONT.render(f"Player {int(player)}'s Turn", 1, "black")
    turnPlayerRect = turnPlayer.get_rect(center=(WIDTH/2, 30))
    WINDOW.blit(turnPlayer, turnPlayerRect)

    for row in rows:
        for stick in row:
            pygame.draw.rect(WINDOW, "brown", stick)

    for button in buttons:
        pygame.draw.rect(WINDOW, "black", button)

    pygame.display.update() # refresh display to update any drawings

def main():
    run = True
    currRow = "None"
    player = 1

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
                # remove stick from row buttons
                if AButton.click() and rowA.numSticks >= 1 and (currRow == "None" or currRow == "A"):
                    rowA.removeStick()
                    currRow = "A"
                if BButton.click() and rowB.numSticks >= 1 and (currRow == "None" or currRow == "B"):
                    rowB.removeStick()
                    currRow = "B"
                if CButton.click() and rowC.numSticks >= 1 and (currRow == "None" or currRow == "C"):
                    rowC.removeStick()
                    currRow = "C"
                if DButton.click() and rowD.numSticks >= 1 and (currRow == "None" or currRow == "D"):
                    rowD.removeStick()
                    currRow = "D"

                # pass turn to other player
                if passButton.click() and currRow != "None":
                    currRow = "None"
                    player = 2 if player == 1 else 1

        totalSticks = rowA.numSticks + rowB.numSticks + rowC.numSticks + rowD.numSticks
        draw(rows, buttons, player)

    pygame.quit()

if __name__ == "__main__":
    main()
