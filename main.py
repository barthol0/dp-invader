import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from hero import Hero
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("DP Invasion")
    #Make a group to store bullets in.
    bullets = Group()

    #Create a hero
    hero = Hero(screen, ai_settings)
    bg_color = (230, 230, 230)

    #main game loop
    while True:
        gf.check_events(hero, ai_settings, screen, bullets)
        hero.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, hero, bullets)

run_game()