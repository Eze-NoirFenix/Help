# Estrellas

import pygame
from pygame.sprite import Sprite

class  bgStars(Sprite):
    def __init__(self, defSettings, Image):
        super(bgStars, self).__init__()
        self.img = Image
        self.defSettings = defSettings

        self.image = pygame.image.load('image/starSamplerz.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.img.blit(self.image, self.rect)
