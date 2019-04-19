import sys

import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the play button.
    play_button = Button(ai_settings, screen, "Play!")
    
    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Make a group of aliens.
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, play_button, ship,
                aliens, bullets)

        if stats.game_active:
            # Update the ship position.
            ship.update()
            # Update any bullet-alien collisions
            gf.check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # Update the bullets on screen.
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # Update the aliens on screen.
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # Update the screen
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
