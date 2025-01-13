import pygame
import pygame.locals
from pygame.locals import *
import random

pygame.init()
s=pygame.display.set_mode((1100,978))
pygame.display.set_caption("Flappy Bird")
f1=pygame.font.SysFont("Arial",75)
c1=(150,45,25)
#variables
fps=70
gscroll=0
scrolls=5
fpipe=1000
fly=False
lastpipe=pygame.time.get_ticks()-fpipe
gameo=False
pipegap=200
score=0
passp=False
clock=pygame.time.Clock()

bg=pygame.image.load("img/bg.png")
ground=pygame.image.load("img/ground.png")
restart=pygame.image.load("img/restart.png")
def text(texts,font,clr,x,y):
    tx=f1.render(texts,True, clr)
    s.blit(tx,(x,y))

class bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for i in range(1,4):
            b1=pygame.image.load(f"img/bird{i}.png")
            self.images.append(b1)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.vel=0
        self.clicked=False
    def update(self):
        if fly==True:
            self.vel+=0.5
            if self.vel>10:
                self.vel=10
            if self.rect.bottom<970:
                self.rect.y+=int(self.vel)
        if gameo==False:
            #jumping of bird
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                self.vel-=10
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
            flap=4
            self.counter+=1
            if self.counter>flap:
                self.counter=0
                self.index+=1
                if self.index>=len(self.images):
                    self.index=0
                self.image=self.images[self.index]
class pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("img/pipe.png")
        self.rect=self.image.get_rect()
        if pos==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-int(pipegap/2)]
        elif pos==-1:
            self.rect.topleft=[x,y+int(pipegap/2)]
    def update(self):
        self.rect.x-=scrolls
        if self.rect.right<0:
            self.kill()
class button():
    def __init__(self,x,y,img):
        self.img=img
        self.rect=self.img.get_rect()
        self.rect.topleft=(x,y)
    def draw(self):
        action=False
        #getting mouse pos
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                action=True
        s.blit(self.img,(self.rect.x,self.rect.y))
        return action
def reset():
    pipegrp.empty()
    objb.rect.x=100
    objb.rect.y=100
    score=0
    return score
pipegrp=pygame.sprite.Group()
birdgrp=pygame.sprite.Group()
objb=bird(100,100)
obj1=button(100,100,restart)
birdgrp.add(objb)
run=True
while run:
    clock.tick(fps)
    s.blit(bg,(0,0))
    birdgrp.draw(s)
    pipegrp.draw(s)
    birdgrp.update()
    #checking the score
    if len(pipegrp)>0:
        if birdgrp.sprites()[0].rect.left>pipegrp.sprites()[0].rect.left\
            and birdgrp.sprites()[0].rect.right>pipegrp.sprites()[0].rect.right\
            and passp==False:
            passp=True
        if passp==True:
            if birdgrp.sprites()[0].rect.left>pipegrp.sprites()[0].rect.right:
                score+=1
                passp=False
    text(str(score),f1,c1,200,200)
    #collison with pipe
    if pygame.sprite.groupcollide(birdgrp,pipegrp,False,False):
        gameo=True
        fly=False
    if fly==True and gameo==False:
        timer=pygame.time.get_ticks()
        if timer-lastpipe>fpipe:
            pipeheigh=random.randint(-50,50)
            bottompipe=pipe(1100,489+pipeheigh,-1)
            toppipe=pipe(1100,489+pipeheigh,1)
            pipegrp.add(bottompipe)
            pipegrp.add(toppipe)
            lastpipe=timer
        pipegrp.update()
        gscroll-=scrolls
        if abs(gscroll)>40:
            gscroll=0
    if gameo==True:
        if obj1.draw():
            gameo=False
            score=reset()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN and fly==False and gameo==False:
            fly=True
    pygame.display.update()
pygame.quit()
