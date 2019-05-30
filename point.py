import random
from random import choice
from globals import *

class Point:
    #As in, the spot on screen, not the score
    def __init__(self):
        self.x = choice([i for i in range(0,SCREEN_WIDTH) if i not in [2,5,7]])
        self.y = choice([i for i in range(0,SCREEN_HEIGHT) if i not in [2,5,7]])
    #The point shall be no more than SCREEN_WIDTH, and no less than 0    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        if x < 0:
            self._x = SCREEN_WIDTH
        elif x > SCREEN_WIDTH:
            self._x = 0
        else:
            self._x = x
            
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        if y < 0:
            self._y = SCREEN_HEIGHT
        elif y > SCREEN_HEIGHT:
            self._y = 0
        else:
            self._y = y