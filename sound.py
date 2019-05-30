import arcade
import random
from collections import deque
from globals import *

class Sound:
    """
    Deals with the Professional and Quality Sound System Used in this AAA Game.
    Soon to be implemented in an Asteroids game near you!
    """
    def __init__(self):
        self.mute = False
        self.captions = True
        self.caption_list = deque()
        self.timer = CAPTION_TIME

        #Pew! Pew!
    def play_pew(self):
        if self.mute == False:
            random_sound = random.randint(1,18)
            sound_switch = {
                1: "pew01.wav", 2: "pew02.wav", 3: "pew03.wav", 4: "pew04.wav",
                5: "pew05.wav", 6: "pew06.wav", 7: "pew07.wav", 8: "pew08.wav",
                9: "pew09.wav", 10: "pew10.wav", 11: "pew11.wav", 12: "pew12.wav",
                13: "pew13.wav"
                }
            sound = arcade.load_sound(sound_switch.get(random_sound, "pew01.wav"))
            arcade.play_sound(sound)
            if len(self.caption_list) == 0:
                self.timer = CAPTION_TIME
            self.caption_list.append("Pew!")
            
    def play_break(self):
        if self.mute == False:
            random_sound = random.randint(1,9)
            sound_switch = {
                1: "break01.wav", 2: "break02.wav", 3: "break03.wav", 4: "break04.wav",
                5: "break05.wav", 6: "break06.wav", 7: "break07.wav", 8: "break08.wav",
                9: "break09.wav"
                }
            sound = arcade.load_sound(sound_switch.get(random_sound, "break01.wav"))
            arcade.play_sound(sound)
            caption_switch = {
                1: "Shatter!", 2: "Crash!", 3: "Checka Sheka",
                4: "Break!", 5: "Crash!", 6: "Kssshhh!", 7: "Break!",
                8: "Shatter!", 9: "Break!"
                }
            if len(self.caption_list) == 0:
                self.timer = CAPTION_TIME
            self.caption_list.append(caption_switch.get(random_sound, "Colby Fetched up the captions"))
            
    def toggle_mute(self):        #If this program is used as inteneded, this function will 
        self.mute = not self.mute #never be called. I intend everyone to hear my voice.
      
    #Captions, just in case somebody deaf plays this game
    def print_captions(self):
        if self.captions == True:
            if self.timer == 0:
                if len(self.caption_list) != 0:
                    self.caption_list.popleft()
                    self.timer = CAPTION_TIME
            else:
                self.timer -= 1
                item = 0
                for caption in self.caption_list:
                        arcade.draw_text(self.caption_list[item], 60 + item * 100, 50, font_size=12, color=arcade.color.BLACK)
                        item += 1
      
    #Captions on/off
    def toggle_captions(self):
        self.captions = not self.captions
    
        