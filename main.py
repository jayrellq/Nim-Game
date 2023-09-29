import pygame
from variables import *
import row
import button

pygame.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Game of Nim")

FONT = pygame.font.SysFont("timesnewroman", 30)

RULES = pygame.image.load("rules.jpg")

def draw(rows, buttons, player):
    WINDOW.fill("gray") # change background color

    # display whose turn is it
    turnPlayer = FONT.render(f"Player {int(player)}'s Turn", 1, "black")
    turnPlayerRect = turnPlayer.get_rect(center=(WIDTH/2, 30))
    WINDOW.blit(turnPlayer, turnPlayerRect)

    for row in rows:
        for stick in row.arr:
            pygame.draw.rect(WINDOW, "yellow", stick)

    playerColor = "red" if player == 1 else "blue"
    for button in buttons:
        pygame.draw.rect(WINDOW, playerColor, button.rect)
        WINDOW.blit(button.text, button.textRect)

    pygame.display.update() # refresh display to update any drawings

def drawHelpScreen(button):
    WINDOW.fill("black")

    title = FONT.render("How to Play", 1, "white")
    titleRect = title.get_rect(center=(WIDTH/2, 30))
    WINDOW.blit(title, titleRect)

    # display the rules image
    WINDOW.blit(RULES, (45, 75))

    # draw a white border
    whiteBorder = pygame.Rect(43, 73, 514, 279)
    pygame.draw.rect(WINDOW, "white", whiteBorder, 2)

    # draw the close button
    pygame.draw.rect(WINDOW, "gray", button.rect)
    buttonText = FONT.render("X", 1, "black")
    buttonTextRect = buttonText.get_rect(center=(button.X + button.width/2, button.Y + button.height/2))
    WINDOW.blit(buttonText, buttonTextRect)

    pygame.display.update()

def main():
    run = True
    currRow = "None"
    player = 1
    winCon = False
    helpScreen = False

    # initialize and create the rows
    rowA = row.Row(1, (WIDTH-STICK_WIDTH)/2, 75)
    rowB = row.Row(3, (WIDTH-STICK_WIDTH)/2, 75)
    rowC = row.Row(5, (WIDTH-STICK_WIDTH)/2, 75)
    rowD = row.Row(7, (WIDTH-STICK_WIDTH)/2, 75)
    rowA.createRow()
    rowB.createRow()
    rowC.createRow()
    rowD.createRow()
    rows = [rowA, rowB, rowC, rowD]

    # initialize and create the buttons
    AButton = button.Button(rowD.Xstart - 100, rowA.Ystart, BUTTON_WIDTH, BUTTON_HEIGHT, FONT, "A")
    BButton = button.Button(rowD.Xstart - 100, rowB.Ystart, BUTTON_WIDTH, BUTTON_HEIGHT, FONT, "B")
    CButton = button.Button(rowD.Xstart - 100, rowC.Ystart, BUTTON_WIDTH, BUTTON_HEIGHT, FONT, "C")
    DButton = button.Button(rowD.Xstart - 100, rowD.Ystart, BUTTON_WIDTH, BUTTON_HEIGHT, FONT, "D")
    passButton = button.Button(rowD.Xend + 50, rowD.Ystart, BUTTON_WIDTH, BUTTON_HEIGHT, FONT, ">")
    helpButton = button.Button(rowD.Xend + 50, rowA.Ystart, BUTTON_WIDTH, BUTTON_HEIGHT, FONT, "?")
    buttons = [AButton, BButton, CButton, DButton, passButton, helpButton]

    while run:
        # check for events
        for event in pygame.event.get():
            # check if window is closed
            if event.type == pygame.QUIT:
                run = False
                break
            # check for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                if helpScreen == False:
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

                        # player that passes with one stick left wins (other player is forced to remove last stick)
                        if totalSticks == 1:
                            winCon = True

                # open help screen
                if helpButton.click():
                    helpScreen = True if helpScreen == False else False

        # calculate total number of sticks left
        totalSticks = rowA.numSticks + rowB.numSticks + rowC.numSticks + rowD.numSticks

        # draw the items on the screen
        if helpScreen:
            drawHelpScreen(helpButton)
        else:
            draw(rows, buttons, player)

        # win con: leave one stick left or other player removes last stick
        if winCon == True or totalSticks == 0:
            player = 2 if player == 1 else 1
            playerColor = "red" if player == 1 else "blue"

            pygame.time.delay(1000)
            winText = FONT.render(f"Player {int(player)} wins!", 1, playerColor)
            wintTextRect = winText.get_rect(center=(WIDTH/2, HEIGHT/2))
            WINDOW.blit(winText,wintTextRect)
            pygame.display.update()
            pygame.time.delay(4000)
            
            # reset game
            currRow = "None"
            player = 1
            winCon = False
            helpScreen = False
            rowA.createRow()
            rowB.createRow()
            rowC.createRow()
            rowD.createRow()

    pygame.quit()

if __name__ == "__main__":
    main()
