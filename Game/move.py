import pygame
pygame.init()
s=pygame.display.set_mode((1150,800))
pygame.display.set_caption("Put ball in net")
class img(pygame.sprite.Sprite):
    def __init__(self,im,x,y):
        super().__init__()
        self.image=pygame.image.load(im)
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
    def hormov(self,p):
        self.rect.x+=5
        if p==1:
            if self.rect.left<=0:
                self.rect.move_ip(-5,0)
        if p==2:
            if self.rect.right>=1150:
                self.rect.move_ip(-5,0)
    def vertmov(self,p):
        self.rect.move_ip(0,5)
        if self.rect.top<=0 and self.rect.bottom>=800:
            self.rect.move_ip(0,-5)
    def update(self,pressed_keys):
        if pressed_keys[pygame.K_w]:
            self.rect.move_ip(0,-5)
        if pressed_keys[pygame.K_s]:
            self.rect.move_ip(0,5)
        if pressed_keys[pygame.K_a]:
            self.rect.move_ip(-5,0)    
        if pressed_keys[pygame.K_d]:
            self.rect.move_ip(5,0)


grp=pygame.sprite.Group()
def startgame():
    obj1=img("fb.png",575,400)
    grp.add(obj1)
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
            p1.vertmov()
        if pressedkeys[pygame.K_s]:
            p1.vertmov()
        if pressedkeys[pygame.K_a]:
            p1.hormov(1)    
        if pressedkeys[pygame.K_d]:
            p1.hormov(1)
        #p2 movement
        if pressedkeys[pygame.K_i]:
            p2.vertmov()
        if pressedkeys[pygame.K_k]:
            p2.vertmov()
        if pressedkeys[pygame.K_j]:
            p2.hormov(2)    
        if pressedkeys[pygame.K_l]:
            p2.hormov(2)
        obj1.update(pressedkeys)
        p1.update(pressedkeys)
        p2.update(pressedkeys)
        s.blit(pygame.image.load("p.png"),(0,0))
        grp.draw(s)
        pygame.display.update()
startgame()
