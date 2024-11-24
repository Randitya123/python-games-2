import pygame
pygame.init()
#defining a screen
s=pygame.display.set_mode((1100,600))
r=True
s.fill((75,145,55))
c1=(42,100,182)
c2=(123,210,23)
c3=(62,173,93)
pygame.display.update()
#class under this comment
class ret():
    def __init__(self,c,d):
        self.surface=s 
        self.color=c
        self.dimension=d
    def draw(self):
        self.drawrect=pygame.draw.rect(self.surface,self.color,self.dimension)
class Circle():
    def __init__(self, c, cord,radius):
        self.surface = s
        self.color = c
        self.radius = radius
        self.cordinate=cord
    def draw(self):
        pygame.draw.circle(self.surface, self.color,self.cordinate,self.radius)
#creating obj
obj1=ret(c1,(45,250,210,162))
obj1.draw()
obj2=ret(c2,(610,400,190,143))
obj2.draw()
obj3=ret(c3,(310,420,120,90))
obj3.draw()

obj4= Circle(c1,(820,400), 50) 
obj4.draw()
obj5= Circle(c2,(75,150), 75) 
obj5.draw()

pygame.display.update()
while r:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            r=False
pygame.quit()
 