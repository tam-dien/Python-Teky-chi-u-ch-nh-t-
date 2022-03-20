import pygame
import math
import random

pygame.init()
sc = pygame.display.set_mode((500,500))
pygame.draw.rect(sc,(121, 186, 0),(0,0,50,50))

class enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.goc = -90
        self.tg_move = 0
        self.tg_random = 0
    def draw(self):
        pygame.draw.rect(sc,(121, 20, 0),(self.x,self.y,50,80))
        ## độ rộng viền sẽ là 5px
        pygame.draw.rect(sc,(255, 0, 0),(self.x + 5,self.y + 5,40,70))
    def move(self):
        ### 1 pixel trên 1 vòng loop
        ### 1 pixel trên 200ms
        if pygame.time.get_ticks() - self.tg_move > 20:
            self.tg_move = pygame.time.get_ticks()
            self.x += math.cos(self.goc/180*math.pi)
            self.y -= math.sin(self.goc/180*math.pi)
            if self.x > 450:
                self.x = 450
            if self.x < 0:
                self.x = 0
            if self.y > 340:
                self.y = 340
            if self.y < 0:
                self.y = 0
        if pygame.time.get_ticks() - self.tg_random > 3000:
            self.tg_random = pygame.time.get_ticks()
            self.goc = random.randint(0,360)

def draw():
    sc.fill((0,0,0))
    pygame.draw.rect(sc,(0,0,255),(0,420,500,10))
    kethu1.draw()
    kethu2.draw()
    pygame.display.update()

def event():
    global run
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            run = False

def runct():
    kethu1.move()
    kethu2.move()

kethu1 = enemy(0,0)
kethu2 = enemy(200,200)

### Chương trình chính
run = True
while run:
    draw()
    runct()
    event()