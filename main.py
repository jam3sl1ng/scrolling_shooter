import pygame

from settings import *
from world import *
from soldier import Soldier

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooter")

player = Soldier(200, 200, 3, 6)

clock = pygame.time.Clock()

def main():
    moving_left = False
    moving_right = False

    run = True
    while run:

        clock.tick(FPS)

        draw_bg(screen)

        player.draw(screen)
        player.update(moving_left, moving_right)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # Keyboard presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving_left = True
                if event.key == pygame.K_d:
                    moving_right = True
            # Keyboard releases
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_d:
                    moving_right = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
