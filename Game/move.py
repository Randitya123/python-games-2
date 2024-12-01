import pygame
pygame.init()
s=pygame.display.set_mode((1100,600))
pygame.display.set_caption("Put ball in net")
class img(pygame.sprite.Sprite):
    def __innit__(self):
        self.image=pygame.image.load("fb.png")
        self.rect=self.image.get_rect()
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
    obj1=img()
    grp.add(obj1)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
        pressedkeys=pygame.key.get_pressed()
        obj1.update(pressedkeys)
        s.blit(pygame.image.load("p.png"),(0,0))
        grp.draw(s)
        pygame.display.update()
startgame()