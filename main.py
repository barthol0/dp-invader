import sys
import pygame
from settings import Settings
from hero import Hero
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("DP Invasion")
    hero = Hero(screen, ai_settings)
    bg_color = (230, 230, 230)

    #main game loop
    while True:
        gf.check_events(hero)
        hero.update()
        gf.update_screen(ai_settings, screen, hero)

run_game()