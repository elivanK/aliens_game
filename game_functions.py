import sys

import pygame

from bullet import Bullet
from alien import Alien 

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
    
def update_bullets(ai_settings, screen, ship, aliens, bullets):
    # Update position of bullets and get rid of old bullets
    # Update bullet positions
    bullets.update()
    
    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
    
def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    # Respond to bullet-alien collisions
    # Remove any bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    # Check if the group aliens is empty
    if len(aliens) == 0:
        # Destroy existing bullets if the aliens group is empty and create a new fleet
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
    
    
            
def get_number_aliens_x(ai_settings, alien_width):
    # Determine the number of aliens that fit in a row
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # Create an alien and place it in the row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width  
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    
            
# Create a full fleet of aliens
def create_fleet(ai_settings, screen, ship, aliens):
    # Create an alien and find the number of aliens in a row
    # Spacing between each alien is equal to one alien width
    # We need to know the aliens width and height in order to place aliens
    # So we create an alien before we perform calculations
    alien = Alien(ai_settings, screen)
    # We get the alien's width from its rect attribue
    # alien_width = alien.rect.width
    # Calculate the horizontal space available for aliens and the number
    # of aliens that can fit into that space
    # available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    # Create the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
    
# How many rows fit in a feet
def get_number_rows(ai_settings, ship_height, alien_height):
    # Determine the number of rows of aliens fit on the screen
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


# Check to see if any aliens are at the left or the right edges
def check_fleet_edges(ai_settings, aliens):
    # Respond appropriately if any aliens have reached an edge 
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
        
def change_fleet_direction(ai_settings, aliens):
    # Drop the entire fleet and change the fleet's direction
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
# We use this method on th aliens group, which automatically call each alien's update method
# Check for collistion between aliens and ship
def update_aliens(ai_settings, ship, aliens):
    # Check if the fleet is at an edge and then update
    # the position of all aliens in the fleet
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    # Look for alien-ship collisions
    # The method spritecollideany() takes two arguments: a sprite and a group.
    if pygame.sprite.spritecollideany(ship, aliens):
        print('Ship hit!!!')
    
    
