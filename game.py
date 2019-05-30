"""
File: Star Wars: Episode 10: The Game: The Movie: The Game: Dark Forces: Hope of the Jedi: Vengance of the Sith: Starfighter: Colon Caner: Republic Commando: Revenge of Darth Maul: Ultimate Edition: &Knuckles.py
Original Author: Br. Burton
Designed to be completed by others
This program implements the Star Wars: Episode 10: The Game: The Movie: The Game: Dark Forces: Hope of the Jedi: Vengance of the Sith: Starfighter: Colon Caner: Republic Commando: Revenge of Darth Maul: Ultimate Edition: &Knuckles game.
"""
import arcade
import math
from asteroid import Asteroid
from small_asteroid import Small_Asteroid
from medium_asteroid import Medium_Asteroid
from large_asteroid import Large_Asteroid
from ship import Ship
from flying_object import Flying_Object
from bullet import Bullet
from sound import Sound
from point import Point
from velocity import Velocity
from konami_code import Konami_Code
from background import background
from globals import *

"""
Did you read the ReadMe? I'd reccomend you do that, as there's a lot to be added to this game.
"""



class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height, "Star Wars: Episode 10: The Game: The Movie: The Game: Dark Forces: Hope of the Jedi: Vengance of the Sith: Starfighter: Colon Caner: Republic Commando: Revenge of Darth Maul: Ultimate Edition: &Knuckles")
        arcade.set_background_color(arcade.color.RED)#SMOKY_BLACK)

        self.held_keys = set()
        
        self.asteroids = []
        self.bullets = []
        self.konami_code = Konami_Code()
        self.ship = Ship()
        self.new_game = True
        self.background = arcade.load_texture("background_main.jpg")
        self.respawn_timer = 0
        self.life_sprite = arcade.Sprite("sprites/blue_falcon.png", .07)
        self.life_sprite.angle = 90
        
        self.sound = Sound()

        # TODO: declare anything here you need the game class to track

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT //2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        
        if self.ship.alive == True and self.ship.lives != 0:
            self.ship.draw()
        # draws one ship in the corner for every life remaining
        i = 0    
        for i in range(self.ship.lives):
            self.life_sprite.center_x = 40 + 70 * i
            self.life_sprite.center_y = 550
            self.life_sprite.update()
            self.life_sprite.draw()
            i += 1
            

        for asteroid in self.asteroids:
            asteroid.draw()
            
        for bullet in self.bullets:
            bullet.draw()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()
        
        # Waits a second or two before respawning the player after a death.
        if self.ship.alive != True:
            self.respawn_timer += 1
            if self.respawn_timer >= 100 and self.ship.lives != 0:
                self.ship.alive = True
                self.ship.reset_position()
                self.respawn_timer = 0
                self.ship.invincible = True
        # RIP
        #Hmmm. This doesn't seem to appear on some images. I'll try to figure out why.
        if self.ship.lives == 0:
            arcade.draw_text("Game Over. Press 'N' to start a New Game", 50, 300, font_size=25, color=arcade.color.NAVY_BLUE)
        
        if self.new_game == True:
            i = 0
            while i != INITIAL_ROCK_COUNT:
                asteroid = Large_Asteroid()
                self.asteroids.append(asteroid)
                i += 1
                self.new_game = False
                
        for asteroid in self.asteroids:
            asteroid.advance()
            
        for bullet in self.bullets:
            bullet.advance()
            
        self.ship.advance()
                

        self.check_collisions()
        
    def check_collisions(self):
        #Checks if bullets (Or ships if you're unlucky) are hitting the asteroids
        for asteroid in self.asteroids:
            
            if self.ship.alive and asteroid.alive:
                    too_close = self.ship.radius + asteroid.radius

                    if (abs(self.ship.center.x - asteroid.center.x) < too_close and
                                abs(self.ship.center.y - asteroid.center.y) < too_close):
                        # its a hit!
                        if self.ship.invincible == False:
                            self.ship.alive = False
                            self.ship.lives -= 1
                            print("Gotem")

            
            for bullet in self.bullets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and asteroid.alive:
                    too_close = bullet.radius + asteroid.radius

                    if (abs(bullet.center.x - asteroid.center.x) < too_close and
                                abs(bullet.center.y - asteroid.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        rock_type = asteroid.hit()
                        
                        if rock_type == "large":
                            medium1 = Medium_Asteroid(asteroid, "up")
                            medium2 = Medium_Asteroid(asteroid, "down")
                            self.asteroids.append(medium1)
                            self.asteroids.append(medium2)
                            small1 = Small_Asteroid(asteroid, "right")
                            self.asteroids.append(small1)
                        elif rock_type == "medium":
                            small1 = Small_Asteroid(asteroid, "up_right")
                            small2 = Small_Asteroid(asteroid, "down_left")
                            self.asteroids.append(small1)
                            self.asteroids.append(small2)

        
        
        self.cleanup_zombies()

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.angle.angle += SHIP_TURN_AMOUNT

        if arcade.key.RIGHT in self.held_keys:
            self.ship.angle.angle -= SHIP_TURN_AMOUNT

        if arcade.key.UP in self.held_keys:
            self.ship.velocity.dx += math.cos(math.radians(self.ship.angle.angle)) * SHIP_THRUST_AMOUNT
            self.ship.velocity.dy += math.sin(math.radians(self.ship.angle.angle)) * SHIP_THRUST_AMOUNT

        if arcade.key.DOWN in self.held_keys:
            pass

        # Machine gun mode...
        if arcade.key.SPACE in self.held_keys:
            if self.konami_code.active == True:
                bullet = Bullet(self.ship)
                self.bullets.append(bullet)


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                bullet = Bullet(self.ship)
                self.bullets.append(bullet)
            
            if key == arcade.key.DOWN:
                print("THE J TRAIN HAS NO BREAKS!!!!!!")
                
        if key == arcade.key.N:
            self.asteroids.clear()
            self.ship.lives = 5
            self.new_game = True
            
        if key == arcade.key.UP:
            self.konami_code.activate("up")
            
        if key == arcade.key.DOWN:
            self.konami_code.activate("down")
            
        if key == arcade.key.LEFT:
            self.konami_code.activate("left")
            
        if key == arcade.key.RIGHT:
            self.konami_code.activate("right")
            
        if key == arcade.key.B:
            self.konami_code.activate("b")
        
        if key == arcade.key.A:
            self.konami_code.activate("a")
            
        if key == arcade.key.RETURN:
            self.konami_code.activate("start")
            
                

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)
            
    def cleanup_zombies(self):
        """
        Removes any dead bullets, asteroids, or ships from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)


# Creates the game and starts it going
background()
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
