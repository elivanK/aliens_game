import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
    # A class to represnet a single alien in the fleet 
    
    def __init__(self, ai_settings, screen):
        # Initialize the alien and set its starting position
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the alien image and set its rect attribute 
        self.image = pygame.image.load('images/crab.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left corner of the screen
        # Add space to the left of it that's equal to the alien's width
        self.rect.x = self.rect.width
        # And a space above it equal to its height
        self.rect.y = self.rect.height
        
        # Store the alien's exact position
        self.x = float(self.rect.x)
    
    def blitme(self):
        # Draw the alien at its current location
        self.screen.blit(self.image, self.rect)
    
    # Check whether an alien is at either edge
    def check_edges(self):
        # Return True if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    # Each time we update the alien position
    # We move it to the right by the amount stored in alien_speed_factor    
    def update(self):
        # Move the alien right or left
        # With self.x we track the alien's exact position
        # and with that value to update position of alien's rect
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x