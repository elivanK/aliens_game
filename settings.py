class Settings():
    # A class to store all settings for the game
    
    def __init__(self):
        # Initialize the game's settings
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        # When ship moves, we adjust its position by 1.5 Pixels 
        self.ship_speed_factor = 1.5
        # The number of ships the player starts
        self.ship_limit = 3
        
        # Bullet settings 
        self.bullet_speed_factor = 3
        self.bullet_width = 2
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        # Store the number of allowed bullets 
        self.bullets_allowed = 100
        
        # Alien settings
        self.alien_speed_factor = 1
        # Creating settings for fleet direction
        # How quickly the fleet drops down the screen each time and aline reaches either edge
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represnets right and -1 left
        self.fleet_direction = 1