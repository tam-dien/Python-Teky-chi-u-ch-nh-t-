import pygame
pygame.init()
sc = pygame.display.set_mode((300,600))
run = True

def draw():
    if run:
        pass

def event():
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            global run
            run = False
            pygame.quit()

while run:
    event()
    draw()