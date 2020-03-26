class GameStats():
    # Track statistics for Alien Invasion
    
    def __init__(self, ai_settings):
        # Initialize statistics
        self.ai_settings = ai_settings
        # Reset some statistics each time the player starts a new game 
        self.reset_stats()
    
        # Start Alien Invasion in an active state to end the game when player runs
        # out of ships 
        self.game_active = False 
        
        
    def reset_stats(self):
        # Initialize statistics that can change during the game
        self.ships_left = self.ai_settings.ship_limit