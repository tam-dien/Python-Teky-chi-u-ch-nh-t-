import pygame
import time
pygame.init()
tg_inhello = 0
tg_inhi = 0
while True:
    if pygame.time.get_ticks() - tg_inhello > 500:
        tg_inhello = pygame.time.get_ticks()
        print('hello')
    if pygame.time.get_ticks() - tg_inhi > 200:
        tg_inhi = pygame.time.get_ticks()
        print('hi')