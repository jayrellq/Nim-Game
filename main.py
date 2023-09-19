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

def createRow(numSticks):
    row = []
    row_X_start = (WIDTH-STICK_WIDTH)/2 - (((numSticks-1)/2) * STICK_WIDTH_SPACE)
    row_X_start_temp = row_X_start
    row_Y_start = 75 + (((numSticks-1)/2) * STICK_HEIGHT_SPACE)

    for i in range(numSticks):
        stick = pygame.Rect(row_X_start, row_Y_start, STICK_WIDTH, STICK_HEIGHT)
        row.append(stick)
        row_X_start += STICK_WIDTH_SPACE

    row_X_end = row_X_start - STICK_WIDTH_SPACE + STICK_WIDTH # remove the added spacing at the end and add stick width
    row_Y_end = row_Y_start + STICK_HEIGHT

    return row, row_X_start_temp, row_X_end, row_Y_start, row_Y_end

def main():
    run = True

    rowA, rowA_X_start, rowA_X_end, rowA_Y_start, rowA_Y_end = createRow(1)
    rowB, rowB_X_start, rowB_X_end, rowB_Y_start, rowB_Y_end = createRow(3)
    rowC, rowC_X_start, rowC_X_end, rowC_Y_start, rowC_Y_end = createRow(5)
    rowD, rowD_X_start, rowD_X_end, rowD_Y_start, rowD_Y_end = createRow(7)

    while run:
        for event in pygame.event.get():
            # check if window is closed
            if event.type == pygame.QUIT:
                run = False
                break
            # check for mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                if pos[0] >= rowA_X_start and pos[0] <= rowA_X_end:
                    if pos[1] >= rowA_Y_start and pos[1] <= rowA_Y_end and len(rowA) >= 1:
                        rowA.pop(0)
                if pos[0] >= rowB_X_start and pos[0] <= rowB_X_end:
                    if pos[1] >= rowB_Y_start and pos[1] <= rowB_Y_end and len(rowB) >= 1:
                        rowB.pop(0)
                if pos[0] >= rowC_X_start and pos[0] <= rowC_X_end:
                    if pos[1] >= rowC_Y_start and pos[1] <= rowC_Y_end and len(rowC) >= 1:
                        rowC.pop(0)
                if pos[0] >= rowD_X_start and pos[0] <= rowD_X_end:
                    if pos[1] >= rowD_Y_start and pos[1] <= rowD_Y_end and len(rowD) >= 1:
                        rowD.pop(0)

        draw(rowA, rowB, rowC, rowD)

    pygame.quit()

if __name__ == "__main__":
    main()
