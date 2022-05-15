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
L_color_vien = [None,red_vien,blue_vien,green_vien,purple_vien,cyan_vien,orange_vien,yellow_vien]

import random

class khoi:
    def __init__(self):
        self.type = random.randint(1,7)
        self.type = 7
        rd_x = 4
        if self.type == 1:
            self.L_block = [[rd_x,-1],[rd_x+1,-1],[rd_x+1,0],[rd_x,0]]
        elif self.type == 2:
            self.L_block = [[rd_x,-2],[rd_x,-1],[rd_x,0],[rd_x+1,0]]
        elif self.type == 3:
            self.L_block = [[rd_x,-2],[rd_x,-1],[rd_x,0],[rd_x-1,0]]
        elif self.type == 4:
            self.L_block = [[rd_x-1,0],[rd_x,0],[rd_x,1],[rd_x,-1]]
        elif self.type == 5:
            self.L_block = [[rd_x-1,-2],[rd_x-1,-1],[rd_x,-1],[rd_x,0]]
        elif self.type == 6:
            self.L_block = [[rd_x,-2],[rd_x-1,-1],[rd_x,-1],[rd_x-1,0]]
        elif self.type == 7:
            self.L_block = [[rd_x-2,-1],[rd_x-1,-1],[rd_x,-1],[rd_x+1,-1]]
        self.time_action = 0
    def draw(self):
        for x,y in self.L_block:
            pygame.draw.rect(sc,L_color[self.type],(x*30,y*30,30,30))
            pygame.draw.rect(sc,L_color_vien[self.type],(x*30,y*30,30,30),2)
    def action(self):
        if pygame.time.get_ticks() - self.time_action > 200:
            self.time_action = pygame.time.get_ticks()
            for i in range(len(self.L_block)):
                self.L_block[i][1] += 1

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
                pygame.draw.rect(sc,L_color_vien[giatri],(x*30,y*30,30,30),2)

def draw():
    if run:
        sc.blit(bg,(0,0))
        draw_diagram()
        khoi1.draw()
        pygame.display.update()

def event():
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            global run
            run = False
            pygame.quit()

def action():
    khoi1.action()

khoi1 = khoi()

while run:
    event()
    action()
    draw()