import pygame

from settings import *

class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)

        self.alive = False

        self.char_type = char_type
        self.action = 0

        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        self.speed = speed
        self.direction = 1
        self.flip = False

        # Animations
        # Idle
        temp_list = []
        for i in range(5):
            img = pygame.image.load(f'img/{self.char_type}/Idle/{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            temp_list.append(img)
        
        self.animation_list.append(temp_list)
        
        temp_list = []
        for i in range(6):
            img = pygame.image.load(f'img/{self.char_type}/Run/{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            temp_list.append(img)
        
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    # Update animations
    def update_animation(self):
        # Update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # Check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # Reset the frame index at the end of the list
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
    
    # Update movement actions
    def update_action(self, new_action):
        # Check if new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # Update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def update(self, moving_left, moving_right):
        # Reset movement variables
        dx = 0
        dy = 0

        # Assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        
        # Check if player is moving and update action
        if self.alive:
            if moving_left or moving_right:
                self.update_action(1) # 1: Run
            else:
                self.update_action(0) # 0: Idle

            # Update rectangle position
            self.rect.x += dx
            self.rect.y += dy

        self.update_animation()

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)