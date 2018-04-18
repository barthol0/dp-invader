import pygame

class Hero():
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('img/hero.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the hero's center
        self.center = float(self.rect.centerx)
        
        #Movement flags
        self.moving_right = False
        self.moving_left = False
        

    def update(self):
        """Update the hero's position based on the movement flags."""
        #Update the hero's center value not the rect.
        if self.moving_right:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += self.ai_settings.hero_speed_factor
        if self.moving_left:
            if self.moving_left and self.rect.left > 0:
                self.center -= self.ai_settings.hero_speed_factor

        #Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)