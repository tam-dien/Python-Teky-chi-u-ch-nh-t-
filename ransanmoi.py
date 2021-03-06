import pygame

pygame.init()

sc = pygame.display.set_mode((400,400))
thua = False
font  = pygame.font.SysFont("arial",50)
font_20  = pygame.font.SysFont("arial",20)
chu_thua = font.render("You Lose!",True,(255,0,0))
cochu_n = chu_thua.get_width()
cochu_c = chu_thua.get_height()
x_chu_thua = 200 - cochu_n/2
y_chu_thua = 200 - cochu_c/2
score = 0

class thucan():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.rect(sc,(0,0,150),(self.x*20,self.y*20,20,20))

class conran:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.huong = 0 #bên phải là 0, trên là 1, trái là 2 và xuống dưới là 3
        self.actiontime = 0
        self.L_duoi = [(x-2,y),(x-1,y)]
    def draw(self):
        pygame.draw.rect(sc,(255,0,0),(self.x*20,self.y*20,20,20))
        for x,y in self.L_duoi:
            pygame.draw.rect(sc,(255,255,255),(x*20,y*20,20,20))
    def event(self,e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                if self.huong != 3:
                    self.huong = 1
            if e.key == pygame.K_DOWN:
                if self.huong != 1:
                    self.huong = 3
            if e.key == pygame.K_LEFT:
                if self.huong != 0:
                    self.huong = 2
            if e.key == pygame.K_RIGHT:
                if self.huong != 2:
                    self.huong = 0
    def action(self):
        #bên phải là 0, trên là 1, trái là 2 và xuống dưới là 3
        if pygame.time.get_ticks() - self.actiontime > 100:
            self.actiontime = pygame.time.get_ticks()
            dutru = self.L_duoi[0]
            self.L_duoi.pop(0)
            self.L_duoi.append((self.x,self.y))
            if self.huong == 0:
                self.x += 1
                if self.x > 19:
                    self.x = 0
            elif self.huong == 1:
                self.y -= 1
                if self.y < 0:
                    self.y = 19
            elif self.huong == 2:
                self.x -= 1
                if self.x < 0:
                    self.x = 19
            else:
                self.y += 1
                if self.y > 19:
                    self.y = 0
            if (self.x,self.y) == (thucan1.x,thucan1.y):
                self.L_duoi.insert(0,dutru)
                thucan1.x = randint(0,19)
                thucan1.y = randint(0,19)
                while (thucan1.x,thucan1.y) in self.L_duoi:
                    thucan1.x = randint(0,19)
                    thucan1.y = randint(0,19)
                global score
                score += 1
            if (self.x,self.y) in self.L_duoi:
                global thua
                thua = True

def action():
    if not thua:
        main.action()

def draw_diem():
    img_diem = font_20.render("Score:"+str(score),True,(255,255,255))
    sc.blit(img_diem,(0,0))

def event():
    global run
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                global thua, main
                if thua:
                    thua = False
                    main = conran(randint(0,19),randint(0,19))
                    global score
                    score = 0
        main.event(e)
## Tạo background
background = pygame.Surface((400,400))
# for y in range(20):
#     for i in range(20):
#         pygame.draw.rect(background,(255,255,255),(i*20,y*20,20,20),1)

def draw():
    sc.blit(background,(0,0))
    thucan1.draw()
    main.draw()
    if thua:
        sc.blit(chu_thua,(x_chu_thua,y_chu_thua))
    draw_diem()
    pygame.display.update()

from random import randint
main = conran(randint(0,19),randint(0,19))
thucan1 = thucan(randint(0,19),randint(0,19))

run = True
while run:
    action()
    draw()
    event()