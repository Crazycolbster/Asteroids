"""
Ah, the classic Konami code. Originally introduced by Japanese game company "Konami" back in the
Nintendo era, this code gave such things as invincibility and infinite lives. In this game,
it unlocks the Super Machine Gun.
"""


class Konami_Code():
    def __init__(self):
        self.up_one = False
        self.up_two = False
        self.down_one = False
        self.down_two = False
        self.left_one = False
        self.right_one = False
        self.left_two = False
        self.right_two = False
        self.b = False
        self.a = False
        self.active = False
        
    def activate(self, button):
        """
        Checks for the spefific combination "Up Up Down Down Left Right Left Right B A Start (Enter)
        If this is entered out of order, this resets the code.
        I might have been able to do this with a list, but I'm not super great at those, so 'if' statements it is.
        """
        
        if button == "up":
##            print("up")
            if self.up_one == False:
                self.up_one = True
            elif self.up_two == False:
                self.up_two = True
            else:
                self.reset()
            
        if button == "down":
#These commented lines for code were used for error checking.
##            print("down")
            if self.up_two == True:
                if self.down_one == False:
                    self.down_one = True
                elif self.down_two == False:
                    self.down_two = True
                else:
                    self.reset()
            else:
                self.reset()
        if button == "left":
##            print("left")
            if self.down_two == True:
                if self.left_one == False:
                    self.left_one = True
                elif self.right_one == True:
                    if self.left_two == False:
                        self.left_two = True
                    else:
                        self.reset()
                else:
                    self.reset()
            else:
                self.reset()
                
        if button == "right":
##            print("right")
            if self.left_one == True:
                if self.right_one == False:
                    self.right_one = True
                elif self.left_two == True:
                    if self.right_two == False:
                        self.right_two = True
                    else:
                        self.reset()
                else:
                    self.reset()
            else:
                self.reset()
                
        if button == "b":
##            print("b")
            if self.right_two == True:
                if self.b == False:
                    self.b = True
                else:
                    self.reset()
            else:
                self.reset()
                
        if button == "a":
##            print("a")
            if self.b == True:
                if self.a == False:
                    self.a = True
                else:
                    self.reset()
            else:
                self.reset()
                
        if button == "start":
##            print("start")
            if self.a == True:
                self.active = True
            else:
                self.reset()
                    
    def reset(self):
##        print("reset")
        self.up_one = False
        self.up_two = False
        self.down_one = False
        self.down_two = False
        self.left_one = False
        self.right_one = False
        self.left_two = False
        self.right_two = False
        self.b = False
        self.a = False