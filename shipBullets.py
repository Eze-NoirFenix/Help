#configuracion de disparo

import pygame
from pygame.sprite import Sprite  # une varios elementos en uno

class Canon(Sprite):  # se encarga de el codigo de las balas
    def __init__(self, defSettings, Image, sttShip):  # da la posicion correcta a Canon
        super(Canon, self).__init__()
        self.screen = Image

        # crea el disparo en la posicion correcta
        self.rect = pygame.Rect(0, 0, defSettings.widBullet, defSettings.heiBullet)
        self.rect.centerx = sttShip.rect.centerx
        self.rect.top = sttShip.rect.top

        # guarda la posicion del disparo en un valor decimal
        self.y = float(self.rect.y)

        self.color = defSettings.rgbBullet
        self.spdFactor = defSettings.speedBullet

    def update(self):  # mueve el disparo hacia arriba
        self.y -= self.spdFactor  #movimiento decimal del disparo
        self.rect.y = self.y  # corrige la posicion del disparo

    def imgBullet (self):  # dibuja el disparo
        pygame.draw.rect(self.screen, self.color, self.rect)
