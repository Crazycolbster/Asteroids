import arcade
from code.asteroid import Asteroid
from code.globals import *

class Large_Asteroid(Asteroid):
    """
    Makes and tracks a big ol asteroid. Not much else to it.
    """
    
    def __init__(self):
        super().__init__()
        self.sprite = arcade.Sprite("sprites/big_rock.png")
        self.radius = BIG_ROCK_RADIUS
        self.sprite.angle = self.angle.angle
            
    def draw(self):
        self.sprite.center_x = self.center.x
        self.sprite.center_y = self.center.y
        self.sprite.update()
        self.sprite.draw()
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        self.sprite.angle += BIG_ROCK_SPIN
        
    def hit(self):
        self.alive = False
        return "large"