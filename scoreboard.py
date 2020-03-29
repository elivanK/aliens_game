import pygame.font

class Scoreboard():
    # A class to report scoring information
    def __init__(self, ai_settings, screen, stats):
        # Initialize scorekeeping attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        # Reprot the tracking value 
        self.stats = stats
        
        # Font settings for scoring information
        self.text_color = (0, 255, 26)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score image
        # This will turn the text to be displayed into an image 
        self.prep_score()
        
    def prep_score(self):
        # Turn the score into a rendered image
        # Round the score to the nearest 10 and store it in rounded_score
        rounded_score = round(self.stats.score, -1)
        # Convert a rounded number to a string with inserted commas
        score_str = "{:,}".format(rounded_score)
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    # Draws the score image to the screen at the location specified by score_rect
    def show_score(self):
        # Draw score to the screen
        self.screen.blit(self.score_image, self.score_rect)    
        