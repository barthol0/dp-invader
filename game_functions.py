import sys
import pygame

def check_events(hero):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                hero.moving_right = True
            elif event.key == pygame.K_LEFT:
                hero.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                hero.moving_right = False
            elif event.key == pygame.K_LEFT:
                hero.moving_left = False

def update_screen(ai_settings, screen, hero):
    """Update images on the screen and flip to the new screen."""
    #Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    hero.blitme()

    #Make the most recently drawn screen visible.
    pygame.display.flip()
