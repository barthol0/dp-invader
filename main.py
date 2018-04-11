import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from hero import Hero
from enemy import Enemy
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("DP Invasion")
    #Make a group of bullets, and a group of enemies.
    bullets = Group()
    enemies = Group()

    #Create a hero
    hero = Hero(screen, ai_settings)
    bg_color = (230, 230, 230)
    #Create a fleet of aliens.
    gf.create_fleet(ai_settings, screen, enemies)

    #main game loop
    while True:
        gf.check_events(hero, ai_settings, screen, bullets)
        hero.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, hero, enemies, bullets)

run_game()