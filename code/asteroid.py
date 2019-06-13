from code.globals import *
from abc import ABC
from abc import abstractmethod
from code.flying_object import Flying_Object
"""
This Asteroid is the template for all asteroids. Just like how all asteroids
in real life share just a couple of characteristics.
"""
class Asteroid(Flying_Object, ABC):
    def __init__(self):
        super().__init__()
        self.alive = True
        self.radius = 30
        
    def hit(self):
        pass
        
