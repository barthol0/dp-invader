import sys
import pygame
from bullet import Bullet

def check_events(hero, ai_settings, screen, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, hero, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, hero)

def check_keydown_events(event, hero, ai_settings, screen, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        hero.moving_right = True
    elif event.key == pygame.K_LEFT:
        hero.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, hero, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, hero):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        hero.moving_right = False
    elif event.key == pygame.K_LEFT:
        hero.moving_left = False


def update_screen(ai_settings, screen, hero, bullets):
    """Update images on the screen and flip to the new screen."""
    #Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    hero.blitme()

    #Redraw all bullets behind hero and enemies.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    #Update bullet positions.
    bullets.update()
    
    #Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))

def fire_bullet(ai_settings, screen, hero, bullets):
    """Fire a bullet if limit not reached yet."""
    #Create a new bullet and add it to the bullets group.
    if len(bullets)< ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, hero)
        bullets.add(new_bullet)
    