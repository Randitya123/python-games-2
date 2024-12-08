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
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
    create()
    pygame.display.update()