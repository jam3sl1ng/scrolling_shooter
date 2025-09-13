import pygame
from settings import *

def draw_bg(screen):
    screen.fill(BG)
    pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300)) # Temporary floor