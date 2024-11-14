import pygame
import random

screen = pygame.display.set_mode((640, 512))


def draw_grid():
    for i in range(1, 16):
        pygame.draw.line(screen,'black',(0, i * 32),(640, i *32)
        )

    for i in range(1, 20):
        pygame.draw.line(screen,'black',(i * 32, 0),(i * 32, 512)
        )


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        clock = pygame.time.Clock()
        running = True

        moleX = 0
        moleY = 0

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickX, clickY = event.pos[0] // 32, event.pos[1] // 32


                    if clickX == moleX //32 and clickY == moleY //32:
                        moleX = ((random.randrange(0, 640)) // 32) *32
                        moleY = ((random.randrange(0, 512)) //32) *32


            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, mole_image.get_rect(topleft=(moleX, moleY)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
