"""
spaceshooter.py
Author: Ethan Adner
Credit: 
ta presence, n'importe ou, me console. Au cas que ton ceour bat, je suis content
mon amour pour toi est eternel et vivante
sans vous, mes 
Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
"""
tutorial4.py
by E. Dennison
"""

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from math import sin, cos, pi

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 700

xli=[]
for x in range(-25,25):
    xli.append(x+500)
yli=[]
for x in range(-25, 25):
    yli.append(x+300)


class sun(Sprite):
    
    asset1 = ImageAsset("images/sun.png")
    height = 50
    width = 50
    
    def __init__(self, position):
        super().__init__(sun.asset1, position)
        
        
        
        
class SpaceShip(Sprite):
    
#    Animated space ship

    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
    Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 0
        self.vy = 0
        self.vr = .0
        self.thrust = 0
        self.thrustframe = 1
    
        SpaceGame.listenKeyEvent("keydown", "q", self.clockwise)
        SpaceGame.listenKeyEvent("keyup", "q", self.stopr)
        SpaceGame.listenKeyEvent("keydown", "e", self.cntrclockwise)
        SpaceGame.listenKeyEvent("keyup", "e", self.stopr)
        SpaceGame.listenKeyEvent("keydown", "space", self.thrustOn)
        SpaceGame.listenKeyEvent("keyup", "space", self.thrustOff)
        
        
        
        self.fxcenter = self.fycenter = 0.5

    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        if self.thrust==1:
            self.vx=50.2*cos(self.rotation+1/2*pi)+self.vx
            self.vy=50.2*sin(self.rotation-1/2*pi)+self.vy
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
            

    def thrustOn(self, event):
        self.thrust = 1
        
    def thrustOff(self, event):
        self.thrust = 0
        
    def stopr(self, event):
        self.vr=0
    
    def clockwise(self, event):
        self.vr=.05
        
    def cntrclockwise(self, event):
        self.vr=-.05
    
    def explode(x, y):
        x=self.x
        y=self.y
        if (x<525 and x>475):
            if (y<325 and y>375):
                SpaceGame.explode(x, y)
            
        
  

        
class SpaceGame(App):
   
    #Tutorial4 space game example.
   
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = ImageAsset("images/starfield.jpg")
        
        
        
        bg1 = Sprite(bg_asset, (0,0))
        bg2 = Sprite(bg_asset, (512,0))
        bg3 = Sprite(bg_asset, (0,512))
        bg4 = Sprite(bg_asset, (512,512))
        bg5 = Sprite(bg_asset, (1024,0))
        bg6 = Sprite(bg_asset, (1024,1024))
        bg7 = Sprite(bg_asset, (1536,1024))
        bg8 = Sprite(bg_asset, (512,512))
        SpaceShip((100,100))
        sun((500,300))
        
        
    def explode(spax, spay):
        expl =  ImageAsset("images/explosion.png")
        ex = Sprite(expl, (spax, spay))
        
        
        

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()