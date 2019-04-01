import sys
import pygame

def check_events(ship):
    """respond to keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
#                 move the ship to right
#                 ship.rect.centerx += 1
                  ship.moving_right = True


def update_screen(ai_settings,screen,ship):
    """update image on the screen and filp to the new screen """
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # make most recently drawn screen
    pygame.display.flip()