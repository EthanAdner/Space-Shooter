"""
spaceshooter.py
Author: Ethan Adner
Credit: 

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

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800


"""class Stars(Sprite):

    asset = ImageAsset("images/starfield.jpg")
    width = 512
    height = 512

    def __init__(self, position):
        super().__init__(Stars.asset, position)

"""
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
        
        """
        SpaceGame.listenKeyEvent("keydown", "d", self.right)
        SpaceGame.listenKeyEvent("keyup", "d", self.stop)
        SpaceGame.listenKeyEvent("keydown", "a", self.left)
        SpaceGame.listenKeyEvent("keyup", "a", self.stop)
        SpaceGame.listenKeyEvent("keydown", "w", self.up)
        SpaceGame.listenKeyEvent("keyup", "w", self.stop)
        SpaceGame.listenKeyEvent("keydown", "s", self.down)
        SpaceGame.listenKeyEvent("keyup", "s", self.stop)
        """
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
            self.vx=.1*cos(self.rotation+1/2*pi)+self.vx
            self.vy=.1*sin(self.rotation-1/2*pi)+self.vy
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
        
        
    """def right(self, event):
        self.vx=1"""
        
    def stopr(self, event):
        self.vr=0
        
    """def stop(self, event):
        self.vx=0
        self.vy=0
        
    def left(self, event):
        self.vx=-1
    
    def up(self, event):
        self.vy=-1
        
    def down(self, event):
        self.vy=1"""
    
    def clockwise(self, event):
        self.vr=.05
        
    def cntrclockwise(self, event):
        self.vr=-.05


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
        SpaceShip((100,100))
        

    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()


myapp = SpaceGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()