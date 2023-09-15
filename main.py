import pygame

WIDTH, HEIGHT = 600, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Game of Nim")

def draw():
    WINDOW.fill("gray") # change background color

    pygame.display.update() # refresh display to update any drawings

def main():
    run = True

    while run:
        # check if window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw()

    pygame.quit()

if __name__ == "__main__":
    main()
