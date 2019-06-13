from code.asteroid import Asteroid
from code.globals import *
import arcade

class Medium_Asteroid(Asteroid):
    """
    Tracks a Medium Asteroid. Simply
    """
    def __init__(self, asteroid, direction):
        super().__init__()
        self.sprite = arcade.Sprite("sprites/medium_rock.png")
        self.radius = MEDIUM_ROCK_RADIUS
        self.sprite.angle = self.angle.angle
        self.center.x = asteroid.center.x
        self.center.y = asteroid.center.y
        #Might have wanted to make these a different list, but I already had the
        #code written when the idea was brought up, and I wanted to add extra features.
        if direction == "up":
            self.velocity.dy = asteroid.velocity.dy + 2
        else:
            self.velocity.dy = asteroid.velocity.dy - 2
        self.velocity.dx = asteroid.velocity.dx
            
    def draw(self):
        self.sprite.center_x = self.center.x
        self.sprite.center_y = self.center.y
        self.sprite.angle += MEDIUM_ROCK_SPIN
        self.sprite.update()
        self.sprite.draw()
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        
    def hit(self):
        self.alive = False
        return "medium"
        
