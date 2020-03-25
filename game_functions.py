import sys

import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # Respond to keypresses
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # When the user press the sapcebar    
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    # Adding keyboard shortcut to end the game via Q
    elif event.key == pygame.K_q:
        sys.exit()
        
def fire_bullet(ai_settings, screen, ship, bullets):
    # Fire a bullet if limit not reached yet
    # Create a new bullet and add it to the bullets group
    # Check how many bullets exist before creating a new bullet
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        

def check_keyup_events(event, ship):
    # Respond to key releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right =  False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False 

def check_events(ai_settings, screen, ship, bullets):
    # Respond to keypress and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
                
# Update the screen
def update_screen(ai_settings, screen, ship, aliens, bullets):
    # Update the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    # To make the ship appear onscreen    
    ship.blitme()
    # To make the aliens appear onscreen
    aliens.draw(screen)
    
    # Make the most recently drawn screen visible
    pygame.display.flip()
    
def update_bullets(bullets):
    # Update position of bullets and get rid of old bullets
    # Update bullet positions
    bullets.update()
    
    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
# Create a full fleet of aliens
def create_fleet(ai_settings, screen, aliens):
    # Create an alien and find the number of aliens in a row
    # Spacing between each alien is equal to one alien width
    