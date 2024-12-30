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
c3=(255,255,255)
c4=(99,44,101)
bord=pygame.Rect(550,0,10,600)
f1=pygame.font.SysFont("Cambria",50)
f2=pygame.font.SysFont("Cambria",75)
#variables
vel=10
velb=5
h1=3
h2=3
rship=pygame.image.load("p1.png")
bship=pygame.image.load("p2.png")
bg=pygame.image.load("bg.jpg")
def create():
    s.blit(bg,(0,0))
    pygame.draw.rect(s,c1,bord)
    hr=f1.render("HEALTH:"+str(h1),1,c2)
    hb=f1.render("HEALTH:"+str(h2),1,c2)
    s.blit(hr,(15,15))
    s.blit(hb,(875,15))
l1=[]
l2=[]
def drawb():
    for i in l1:
        pygame.draw.rect(s,c3,i)
        i.x+=velb
    for d in l2:
        pygame.draw.rect(s,c3,d)
        d.x-=velb
redhit=pygame.USEREVENT+1
bluehit=pygame.USEREVENT+2
def handleb():
    global h1, h2
    for bullet in l1:
        if r.rect.colliderect(bullet):
            h1-=1
            l1.remove(bullet)
            break
        elif bullet.x<0:
            l1.remove(bullet)
    for bullet in l2:
        if b.rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(redhit))
            h2-=1
            l2.remove(bullet)
            break
        elif bullet.x>1100:
            l2.remove(bullet)
    for bullet in l1:
        for bullett in l2:
            if bullet.colliderect(bullett):
                l1.remove(bullet)
                l2.remove(bullett)
class players(pygame.sprite.Sprite):
    def __init__(self,image,posx,posy):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=posx
        self.rect.y=posy
    def hormov(self,speed,p):
        self.rect.x+=speed
        if p==1:
            if self.rect.left<=0 or self.rect.right>=bord.left:
                self.rect.move_ip(-speed,0)
        if p==2:
            if self.rect.right>=1110 or self.rect.left<=bord.right:
                self.rect.move_ip(-speed,0)
    def vertmov(self,speed):
        self.rect.move_ip(0,speed)
        if self.rect.top<=0 or self.rect.bottom>=600:
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
        if event.type==KEYDOWN:
            if event.key==K_LCTRL:
                bullet=pygame.Rect(r.rect.x+r.rect.width,r.rect.y+r.rect.height//2,25,25)
                l1.append(bullet)
            if event.key==K_RCTRL:
                bullet=pygame.Rect(b.rect.x,b.rect.y+b.rect.y+b.rect.height,25,25)
                l2.append(bullet)   
        if event.type==redhit:
            h1-=1
        if event.type==bluehit:
            h2-=1
    key=pygame.key.get_pressed()
    if key[K_w]:
        r.vertmov(-1)
    if key[K_s]:
        r.vertmov(1)
    if key[K_a]:
        r.hormov(-1,1)
    if key[K_d]:
        r.hormov(1,1)

    if key[K_i]:
        b.vertmov(-1)
    if key[K_k]:
        b.vertmov(1)
    if key[K_j]:
        b.hormov(-1,2)
    if key[K_l]:
        b.hormov(1,2)
    create()
    grp.draw(s)
    drawb()
    handleb()
    pygame.display.update()
