class Angle():
    """
    Angles we have set on high, sweetly spinning o'er the game.
    And the setters in reply, say no more than 360.
    """
    def __init__(self):
        self.angle = 90
    @property
    def angle(self):
        return self._angle
    
    @angle.setter
    def angle(self, angle):
        if angle < 0:
            self._angle += 360
        elif angle > 360:
            self._angle -= 360
        else:
            self._angle = angle
