from asteroid import Asteroid
from globals import *
import arcade

class Small_Asteroid(Asteroid):
    """
    Baby Asteroid do do do do do do
    Baby Asteroid do do do do do do
    Baby Asteroid do do do do do do
    Baby Asteroid!
    """
    def __init__(self, asteroid, direction):
        super().__init__()
        self.sprite = arcade.Sprite("sprites/small_rock.png")
        self.radius = SMALL_ROCK_RADIUS
        self.sprite.angle = self.angle.angle
        self.center.x = asteroid.center.x
        self.center.y = asteroid.center.y
        if direction == "right":
            self.velocity.dx = asteroid.velocity.dx + 5
            self.velocity.dy = asteroid.velocity.dy
        elif direction == "up_right":
            self.velocity.dy = asteroid.velocity.dy + 1.5
            self.velocity.dx = asteroid.velocity.dx + 1.5
        elif direction == "down_left":
            self.velocity.dy = asteroid.velocity.dy - 1.5
            self.velocity.dx = asteroid.velocity.dx - 1.5
            
    def draw(self):
        self.sprite.center_x = self.center.x
        self.sprite.center_y = self.center.y
        self.sprite.angle += SMALL_ROCK_SPIN
        self.sprite.update()
        self.sprite.draw()
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        
    def hit(self):
        self.alive = False
        


