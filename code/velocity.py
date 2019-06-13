import random
from code.globals import *

class Velocity:
    """
    Choses and tracks psudo-random directions for objects to move in.
    """
    def __init__(self):
        self.dx = random.uniform (-BIG_ROCK_SPEED,BIG_ROCK_SPEED)
        self.dy = random.uniform (-BIG_ROCK_SPEED,BIG_ROCK_SPEED)
    