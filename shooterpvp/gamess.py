import pygame
from pygame.locals import*
import os
pygame.font.init()
pygame.mixer.init()
s=pygame.display.set_mode((1100,600))
pygame.display.set_caption("s p a c e")
#colors
c1=(150,220,60)
c2=(75,25,150)
c3=(34,85,99)
c4=(99,44,101)
bord=pygame.Rect(550,0,10,600)
f1=pygame.font.SysFont("Cambria",50)
f2=pygame.font.SysFont("Cambria",75)
#variables
vel=10
velb=15
h1=3
h2=3
rship=pygame.image.load("p1.png")
bship=pygame.image.load("p2.png")
bg=pygame.image.load("bg.jpg")
def create():
    s.blit(bg,(0,0))
class players(pygame.sprite.Sprite):
    def __init__(self,image,posx,posy):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=posx
        self.rect.y=posy
    def hormov(self,speed,p):
        self.rect.x=speed
        if p==1:
            if self.rect.left<=0 and self.rect.right>=bord.left:
                self.rect.move_ip(-speed,0)
        if p==2:
            if self.rect.right>=1110 and self.rect.left<=bord.right:
                self.rect.move_ip(-speed,0)
    def vertmov(self,speed):
        self.rect.move_ip(0,speed)
        if self.rect.top<=0 and self.rect.bottom>=600:
                self.rect.move_ip(0,-speed)
r=players(rship,275,300)
b=players(bship,825,300)
grp=pygame.sprite.Group()
grp.add(r)
grp.add(b)
while True: 
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
    key=pygame.key.get_pressed()
    if key[K_w]:
        r.vertmov(-3)
    if key[K_s]:
        r.vertmov(3)
    if key[K_a]:
        r.hormov(-3,1)
    if key[K_d]:
        r.hormov(3,1)

    if key[K_UP]:
        b.vertmov(-3)
    if key[K_DOWN]:
        b.vertmov(3)
    if key[K_LEFT]:
        b.hormov(-3,2)
    if key[K_RIGHT]:
        b.hormov(3,2)
    create()
    grp.draw(s)
    pygame.display.update()
