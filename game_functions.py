import sys

import pygame

def check_events(ship):
    # Respond to keypress and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # When the right arrow key is pressed
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right
                ship.moving_right = True
            # Move the ship to the left
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
                
# Update the screen
def update_screen(ai_settings, screen, ship):
    # Update the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # Make the most recently drawn screen visible
    pygame.display.flip()