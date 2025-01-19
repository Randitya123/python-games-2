import pygame, random, time
from pygame.locals import*
pygame.init()
pygame.display.set_caption("Recycle Game")
s=pygame.display.set_mode((1100,600))
run=True
score=0
timer=time.time()
clock=pygame.time.Clock()
f1=pygame.font.SysFont("Times New Roman",25)
holdf=f1.render("Score:"+str(score),True,"black")

bg=pygame.image.load("bg.jpg")
class bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("p1.png")
        self.rect=self.image.get_rect()
obj1=bin()
grp=pygame.sprite.Group()
grp.add(obj1)

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    s.blit(bg,(0,0))
    s.blit(holdf,(0,0))
    grp.draw(s)
    pygame.display.update()
pygame.quit()
