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
fps=240
gscroll=0
scrolls=5
fly=False
gameo=False
pipegap=100
fpipe=1000
score=0
passp=False
clock=pygame.time.Clock()

bg=pygame.image.load("img/bg.png")
ground=pygame.image.load("img/ground.png")
restart=pygame.image.load("img/restart.png")

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
            self.vel+=1.5
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
                self.clicked=True
            flap=4
            self.counter+=1
            if self.counter>flap:
                self.counter=0
                self.index+=1
                if self.index>=len(self.images):
                    self.index=0
                self.image=self.images[self.index]
birdgrp=pygame.sprite.Group()
objb=bird(100,100)
birdgrp.add(objb)
run=True
while run:
    clock.tick(fps)
    s.blit(bg,(0,0))
    birdgrp.draw(s)
    birdgrp.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN and fly==False and gameo==False:
            fly=True
    pygame.display.update()
pygame.quit()
