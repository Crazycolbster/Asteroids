from flying_object import Flying_Object
import math
import arcade
from globals import *
"""
Makes and uses the Bullets in the game. Future plans involve adding more bullet types, but for now,
I have a Math class to study for.
"""


class Bullet(Flying_Object):
    def __init__(self,ship):
        super().__init__()
        self.alive = True
        self.center.x = ship.center.x
        self.center.y = ship.center.y
        self.velocity.dx = ship.velocity.dx + math.cos(math.radians(ship.angle.angle)) * BULLET_SPEED
        self.velocity.dy = ship.velocity.dy + math.sin(math.radians(ship.angle.angle)) * BULLET_SPEED
        """
        It's worth noting that if you want to use the original laser instead, you can replace the code with that in
        the comment. I have not, as it's hilarious to fire copys of your ship.
        """
        self.sprite = arcade.Sprite("sprites/blue_falcon.png", .07) ## arcade.Sprite("sprites/laserBlue01.png")
        self.frames = BULLET_LIFE
        self.angle.angle = ship.angle.angle
        self.radius = BULLET_RADIUS
        
    def draw(self):
        self.sprite.center_x = self.center.x
        self.sprite.center_y = self.center.y
        self.sprite.angle = self.angle.angle
        self.sprite.update()
        self.sprite.draw()
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        if self.frames != 0:
            self.frames -=1  #Keeps track of how long the bullet is alive and marks it dead after 60 frames.
        else:
            self.alive = False

        
