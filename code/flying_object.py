from abc import ABC
from abc import abstractmethod
from code.point import Point
from code.velocity import Velocity
from code.angle import Angle
"""
But are you really flying if you're in space?
I like to think of it as "Falling in Style"
"""
class Flying_Object(ABC):
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.angle = Angle()
        
    