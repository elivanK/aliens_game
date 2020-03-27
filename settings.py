class Settings():
    # A class to store all settings for the game
    
    def __init__(self):
        # Initialize the game's static settings
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        
        # Ship settings
        # The number of ships the player starts
        self.ship_limit = 3
        
        # Bullet settings 
        self.bullet_width = 2
        self.bullet_height = 10
        self.bullet_color = 0, 255, 26
        # Store the number of allowed bullets 
        self.bullets_allowed = 3
        
        # Alien settings 
        # How quickly the fleet drops down the screen each time and aline reaches either edge
        self.fleet_drop_speed = 10
        
        # How quicly the game speeds up
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
        
        
    def initialize_dynamic_settings(self):
        # Initialize settings that change throughout the game
        # When ship moves, we adjust its position by 1.5 Pixels 
        self.ship_speed_factor = 1.5
        # Bullet settings 
        self.bullet_speed_factor = 3
        # Alien settings
        self.alien_speed_factor = 1
        # fleet_direction of 1 represnets right and -1 left
        self.fleet_direction = 1
        
    # To increase the speeds of the ship, bullets, and aliens each time
    # the player reaches a new level
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        
        
        
        
        