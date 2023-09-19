import pygame

WIDTH, HEIGHT = 600, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Game of Nim")

STICK_WIDTH, STICK_HEIGHT = 10, 50

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
    stick = pygame.Rect(rowA_X, 75, STICK_WIDTH, STICK_HEIGHT)
    rowA.append(stick)

    rowB = []
    rowB_X = rowA_X - 50
    for i in range(3):
        stick = pygame.Rect(rowB_X, 150, STICK_WIDTH, STICK_HEIGHT)
        rowB.append(stick)
        rowB_X += 50
    
    rowC = []
    rowC_X = rowA_X - 100
    for i in range(5):
        stick = pygame.Rect(rowC_X, 225, STICK_WIDTH, STICK_HEIGHT)
        rowC.append(stick)
        rowC_X += 50
    
    rowD = []
    rowD_X = rowA_X - 150
    for i in range(7):
        stick = pygame.Rect(rowD_X, 300, STICK_WIDTH, STICK_HEIGHT)
        rowD.append(stick)
        rowD_X += 50

    while run:
        # check if window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(rowA, rowB, rowC, rowD)

    pygame.quit()

if __name__ == "__main__":
    main()
