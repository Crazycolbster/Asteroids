from code.flying_object import Flying_Object
import arcade
import math
from code.globals import *

class Ship(Flying_Object):
    """
    Deals with the Blue Falcon, the ship the player controls.
    """
    def __init__(self):
        #Goodness, there's sure a lot of these.
        super().__init__()
        self.lives = 5
        self.sprite = arcade.Sprite("sprites/blue_falcon.png", .07)
        self.alive = True
        self.velocity.dx = 0
        self.velocity.dy = 0
        self.center.x = SCREEN_WIDTH / 2
        self.center.y = SCREEN_HEIGHT / 2
        self.radius = SHIP_RADIUS
        self.invincible = False
        self.invincible_frames = 0
        self.invisible = False
    
    def draw(self):
        self.sprite.center_x = self.center.x
        self.sprite.center_y = self.center.y
        self.sprite.angle = self.angle.angle
        self.sprite.update()
        if self.invisible == False:
            self.sprite.draw()
        
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        #The ship flashes when it respawns.
        if self.invincible == True:
            if self.invincible_frames < 100:
                self.invincible_frames += 1
                if self.invincible_frames % 2 == 0:
                    self.invisible = False
                else:
                    self.invisible = True
            else:
                self.invincible = False
                self.invincible_frames = 0
                
        
    def reset_position(self):
        #Either a new game, or you died.
        self.center.x = SCREEN_WIDTH / 2
        self.center.y = SCREEN_HEIGHT / 2
        self.velocity.dx = 0
        self.velocity.dy = 0