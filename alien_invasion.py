""" We create an ampty Pygame window - the basic structure of a game"""

import pygame
from pygame.sprite import Group

from settings import Settings 
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in
    bullets = Group()
    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        
        # Ged rid of bullets that have disappeared
        # Don't remove items from a list of group within a for loop but a copy of it is fine
        for bullet in bullets.copy():
            # Check if the bullet has disappered of the stop of the screen
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        # Show how many bullets currenty exist in the game and verify they're deleted        
        print(len(bullets))
        
        gf.update_screen(ai_settings, screen, ship, bullets)
        

run_game()
