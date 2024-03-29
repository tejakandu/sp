import pygame

# class ship():
#     def__init__(self,screen):
#     """inisilize the ship and set its starting position"""
#         self.screen = screen

class Ship():
    def __init__(self,screen):
        """inisilize the ship and set its starting position"""
        self.screen = screen
        # load the ship image a get it rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


        # movement flag
        self.moving_right = False
    def update(self):
        """update the ship position based on the movement flag"""
        if self.moving_right:
            self.rect.centerx +=1

    def blitme(self):
        """draw the ship at its current position"""
        self.screen.blit(self.image,self.rect)
        # print("hi")