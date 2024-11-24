import pgzrun,random
TITLE="Gravity Ball"
WIDTH=1600
HEIGHT=900
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
c=r,g,b
grav=2000

class circle1():
    def __init__(self,x,y):
        self.color=c
        self.cordinatex=x
        self.cordinatey=y
        self.radius=90
        self.velx=200
        self.vely=0
    def draw(self):
        pos=(self.cordinatex, self.cordinatey)
        screen.draw.filled_circle(pos,self.radius,c)
obj1=circle1(150,500)
def draw():
    obj1.draw()
def update(dt):
    global obj1
    uy=obj1.vely
    obj1.vely+=grav*dt
    obj1+=(uy+obj1.vely)*0.5*dt
    #detect and handle bounce
    if obj1.y>HEIGHT-obj1.radius:
        obj1.y=HEIGHT-obj1.radius
        obj1.vely=-obj1.vely*0.9
    obj1.x+=obj1.velx*dt
def on_key_down(key):
    if key==keys.SPACE:
        obj1.vely=-500

pgzrun.go()
