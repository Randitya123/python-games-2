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
class recyclable(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
class nonrecyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("plastic.png")
        self.rect=self.image.get_rect()
l1=["biobag.png","foood.png","paper.png"]
obj1=bin()
grp=pygame.sprite.Group()
recyclablegrp=pygame.sprite.Group()
nonrecyclablegrp=pygame.sprite.Group()
grp.add(obj1)
for i in range(25):
    obj2=recyclable(random.choice(l1))
    obj2.rect.x=random.randint(100,1000)
    obj2.rect.y=random.randint(100,500)
    grp.add(obj2)
    recyclablegrp.add(obj2)
for z in range(30):
    obj3=nonrecyclable()
    obj3.rect.x=random.randint(100,1000)
    obj3.rect.y=random.randint(100,500)
    grp.add(obj3)
    nonrecyclablegrp.add(obj3)
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    keypressed=pygame.key.get_pressed()
    if keypressed[K_w]:
        obj1.rect.y-=5
    if keypressed[K_s]:
        obj1.rect.y+=5
    if keypressed[K_a]:
        obj1.rect.x-=5
    if keypressed[K_d]:
        obj1.rect.x+=5
    recyclecollide=pygame.sprite.spritecollide(obj1,recyclablegrp,True)
    for i in recyclecollide:
        score+=1
        holdf=f1.render("Score:"+str(score),True,"black")
    s.blit(bg,(0,0))
    s.blit(holdf,(0,0))
    grp.draw(s)
    pygame.display.update()
pygame.quit()
