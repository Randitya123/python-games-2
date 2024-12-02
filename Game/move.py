import pygame
pygame.init()
s=pygame.display.set_mode((1150,800))
pygame.display.set_caption("Put ball in net")
point1=0
point2=0 
class img(pygame.sprite.Sprite):
    def __init__(self,im,x,y):
        super().__init__()
        self.image=pygame.image.load(im)
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
    def hormov(self,speed,p):
        self.rect.x+=speed
        if p==1:
            if self.rect.left<=0:
                self.rect.move_ip(-speed,0)
        if p==2:
            if self.rect.right>=1150:
                self.rect.move_ip(-speed,0)
    def vertmov(self,speed):
        self.rect.move_ip(0,speed)
        if self.rect.top<=0 and self.rect.bottom>=800:
            self.rect.move_ip(0,-speed)
class move(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("fb.png")
        self.rect=self.image.get_rect()
        self.velocity=[3,3]
    def update(self):
        self.rect.move_ip(self.velocity)
        if self.rect.left<=0 or self.rect.right>=1150:
            self.velocity[0]=-self.velocity[0]
        if self.rect.top<=0 or self.rect.bottom>=800  :
            self.velocity[1]=-self.velocity[1]
grp=pygame.sprite.Group()
grp2=pygame.sprite.Group()
grp3=pygame.sprite.Group()
def startgame():
    b=move()
    grp.add(b)
    p1=img("r.png",50,380)
    p2=img("m.png",950,380)
    grp.add(p1)
    grp.add(p2) 
    while True: 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
        pressedkeys=pygame.key.get_pressed()
        if pressedkeys[pygame.K_w]:
            p1.vertmov(-5)
        if pressedkeys[pygame.K_s]:
            p1.vertmov(5)
        if pressedkeys[pygame.K_a]:
            p1.hormov(-5,1)    
        if pressedkeys[pygame.K_d]:
            p1.hormov(5,1)
        #p2 movement
        if pressedkeys[pygame.K_i]:
            p2.vertmov(-5)
        if pressedkeys[pygame.K_k]:
            p2.vertmov(5)
        if pressedkeys[pygame.K_j]:
            p2.hormov(-5,2)    
        if pressedkeys[pygame.K_l]:
            p2.hormov(5,2)

        grp.update()
        p1.update(pressedkeys)
        p2.update(pressedkeys)
        s.blit(pygame.image.load("p.png"),(0,0))
        col=pygame.sprite.grp()
        grp.draw(s)
        pygame.display.update()
startgame()
