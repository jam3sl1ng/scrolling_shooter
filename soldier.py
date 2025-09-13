import pygame
import os

from settings import *

class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, jump_force):
        pygame.sprite.Sprite.__init__(self)

        self.alive = True

        self.char_type = char_type
        self.action = 0

        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        self.speed = speed
        self.jump_force = jump_force
        self.vel_y = 0

        self.in_air = True
        self.direction = 1
        self.flip = False
        self.jump = False

        # Animations
        animation_types = ['Idle', 'Run', 'Jump']
        for animation in animation_types:
            temp_list = [] # Reset temporary list of images

            num_of_frames = len(os.listdir(f'img/{self.char_type}/{animation}')) # Count the number of frames in each animation folder
            
            for i in range(num_of_frames):
                img = pygame.image.load(f'img/{self.char_type}/{animation}/{i}.png')
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
        
        # Jumping
        if self.jump == True and self.in_air == False:
            self.vel_y = -self.jump_force
            self.jump = False
            self.in_air = True
        
        # Check if player is moving and update action
        if self.alive:
            if self.in_air:
                self.update_action(2) # 2: Jump
            elif moving_left or moving_right:
                self.update_action(1) # 1: Run
            else:
                self.update_action(0) # 0: Idle

            # Update rectangle position
            self.vel_y += GRAVITY # Apply gravity
            if self.vel_y > 10:
                self.vel_y # Stop gravity accelerating past 10
            dy += self.vel_y

            # Check collision with the temporary floor
            if self.rect.bottom + dy > 300:
                dy = 300 - self.rect.bottom
                self.in_air = False

            self.rect.x += dx
            self.rect.y += dy

        self.update_animation()

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)