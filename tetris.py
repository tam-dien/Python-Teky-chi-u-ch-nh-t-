import pygame
pygame.init()
sc = pygame.display.set_mode((300,600))
run = True

red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
purple = (128,0,128)
cyan = (0,255,255)
orange = (255,165,0)
yellow = (255,255,0)
red_vien = (165,0,0)
blue_vien = (0,0,165)
green_vien = (0,165,0)
purple_vien = (50,0,50)
cyan_vien = (0,165,165)
orange_vien = (165,70,0)
yellow_vien = (165,165,0)

L_color = [None,red,blue,green,purple,cyan,orange,yellow]
L_covor_vien = [None,red_vien,blue_vien,green_vien,purple_vien,cyan_vien,orange_vien,yellow_vien]

import random

class khoi:
    def __init__(self):
        self.type = random.randint(1,7)
        if self.type == 1:
            rd_x = random.randint(0,8)
            self.L_block = [(rd_x,-1),(rd_x+1,-1),(rd_x+1,0),(rd_x,0)]

L_diagram = []
for i in range(20):
    L_diagram.append([0]*10)

bg = pygame.Surface((300,600))
for x in range(10):
    for y in range(20):
        pygame.draw.rect(bg,(255,255,255),(x*30,y*30,30,30),2)

def draw_diagram():
    for x in range(10):
        for y in range(20):
            if L_diagram[y][x] != 0:
                giatri = L_diagram[y][x]
                pygame.draw.rect(sc,L_color[giatri],(x*30,y*30,30,30))
                pygame.draw.rect(sc,L_covor_vien[giatri],(x*30,y*30,30,30),2)

def draw():
    if run:
        sc.blit(bg,(0,0))
        draw_diagram()
        pygame.display.update()

def event():
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            global run
            run = False
            pygame.quit()

while run:
    event()
    draw()