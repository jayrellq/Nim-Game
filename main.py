import pygame

WIDTH, HEIGHT = 600, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Game of Nim")

STICK_WIDTH, STICK_HEIGHT = 10, 50
STICK_WIDTH_SPACE, STICK_HEIGHT_SPACE = 50, 75

def draw(rowA, rowB, rowC, rowD):
    WINDOW.fill("gray") # change background color

    rows = [rowA, rowB, rowC, rowD]
    for row in rows:
        for stick in row:
            pygame.draw.rect(WINDOW, "brown", stick)

    pygame.display.update() # refresh display to update any drawings

def main():
    run = True

    rowA = []
    rowA_X = (WIDTH - STICK_WIDTH) / 2
    rowA_Y = 75
    stick = pygame.Rect(rowA_X, rowA_Y, STICK_WIDTH, STICK_HEIGHT)
    rowA.append(stick)

    rowB = []
    rowB_X = rowA_X - STICK_WIDTH_SPACE
    rowB_Y = rowA_Y + STICK_HEIGHT_SPACE
    for i in range(3):
        stick = pygame.Rect(rowB_X, rowB_Y, STICK_WIDTH, STICK_HEIGHT)
        rowB.append(stick)
        rowB_X += STICK_WIDTH_SPACE
    
    rowC = []
    rowC_X = rowA_X - 2*STICK_WIDTH_SPACE
    rowC_Y = rowA_Y + 2*STICK_HEIGHT_SPACE
    for i in range(5):
        stick = pygame.Rect(rowC_X, rowC_Y, STICK_WIDTH, STICK_HEIGHT)
        rowC.append(stick)
        rowC_X += STICK_WIDTH_SPACE
    
    rowD = []
    rowD_X = rowA_X - 3*STICK_WIDTH_SPACE
    rowD_Y = rowA_Y + 3*STICK_HEIGHT_SPACE
    for i in range(7):
        stick = pygame.Rect(rowD_X, rowD_Y, STICK_WIDTH, STICK_HEIGHT)
        rowD.append(stick)
        rowD_X += STICK_WIDTH_SPACE

    while run:
        # check if window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if pos[0] >= rowA_X - 3*STICK_WIDTH_SPACE and pos[0] <= (WIDTH+STICK_WIDTH)/2 + 3*STICK_WIDTH_SPACE:
                if pos[1] >= rowA_Y and pos[1] <= rowA_Y + STICK_HEIGHT:
                    print("rowA:", pos)
                elif pos[1] >= rowB_Y and pos[1] <= rowB_Y + STICK_HEIGHT:
                    print("rowB:", pos)
                elif pos[1] >= rowC_Y and pos[1] <= rowC_Y + STICK_HEIGHT:
                    print("rowC:", pos)
                elif pos[1] >= rowD_Y and pos[1] <= rowD_Y + STICK_HEIGHT:
                    print("rowD:", pos)

        draw(rowA, rowB, rowC, rowD)

    pygame.quit()

if __name__ == "__main__":
    main()
