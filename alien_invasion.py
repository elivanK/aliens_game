""" We create an ampty Pygame window - the basic structure of a game"""

import pygame
from pygame.sprite import Group

from settings import Settings 
from game_stats import GameStats
from ship import Ship

import game_functions as gf

def run_game():
    # Initialize pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Create an instance to store game statistics
    stats = GameStats(ai_settings)

    # Make a ship, a group of bullets and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Start the main loop for the game and call to update the ship, bullets and 
    # position of each alien
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets) 
        # The arguments will be used to track the  number of ships the player
        # has left and to build a new fleet whne an alien hits the ship
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)       
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        

run_game()
