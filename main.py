import pygame

from settings import *
from world import *
from soldier import Soldier

pygame.init()
   
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooter")

clock = pygame.time.Clock()

player = Soldier('player', 200, 200, 3, 6, 11)
enemy = Soldier('enemy', 400, 200, 3, 6, 0)

bullet_img = pygame.image.load('img/icons/bullet.png').convert_alpha()
bullet_group = pygame.sprite.Group()

def main():
    moving_left = False
    moving_right = False

    run = True
    while run:

        clock.tick(FPS)

        draw_bg(screen)
 
        enemy.draw(screen)

        player.draw(screen)
        player.update(moving_left, moving_right, screen, bullet_img, bullet_group)

        # Update and draw groups
        bullet_group.update()
        bullet_group.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # Keyboard presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving_left = True
                if event.key == pygame.K_d:
                    moving_right = True
                if event.key == pygame.K_SPACE:
                    player.jump = True
                if event.key == pygame.K_w:
                    player.shoot = True
                if event.key == pygame.K_ESCAPE:
                    run = False
            # Keyboard releases
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_d:
                    moving_right = False
                if event.key == pygame.K_w:
                    player.shoot = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
