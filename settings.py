class Settings():
    # A class to store all settings for the game
    
    def __init__(self):
        # Initialize the game's settings
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        # When ship moves, we adjust its position by 1.5 Pixels 
        self.ship_speed_factor = 1.5
        
        # Bullet settings 
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60