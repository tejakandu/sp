import sys

import pygame as pygame
from settings import settings
from ship import Ship
import game_function as gf



def run_game():
    #inisilize game and create a screen object and seetings from setiings class
    pygame.init()
    ai_settings = settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("alien invasion")

    # make a ship
    ship = Ship(screen)

    # start main loop for the game
    while True:
    #     watch for keyboard and mouse inputs
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             sys.exit()


        gf.check_events(ship)
        ship.update()

    # redraw the screen each pass through the loop
    #     screen.fill(ai_settings.bg_color)
    #     ship.blitme()

        gf.update_screen(ai_settings,screen,ship)

    # make the most recent drawn screen visible
    #     pygame.display.flip()
run_game()





