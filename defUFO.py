# nave enemiga
import pygame
from pygame.sprite import Sprite  # Pygame sprites must have a self.image and a self.rect

class ufoShip(Sprite):  # class que representa los enemigos
    def __init__(self, defSettings, Image):  # deja la nave en su posicion inicial
        super(ufoShip, self).__init__()
        self.img = Image
        self.defSettings = defSettings

        # carga la imagen del enemigo recto
        self.image = pygame.image.load('image/defUFO.bmp')
        self.rect = self.image.get_rect()

        # inicia el enemigo arriba
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # almacena el enemigo en una posicion exacta
        self.x = float(self.rect.x)

    def blitme(self):
        # dibuja el enemigo
        self.img.blit(self.image, self.rect)

    def chkEdge(self):
        # vuelve al enemigo al borde de pantalla
        rImage = self.image.get_rect()
        if self.rect.right >= rImage.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        # move UFO derecha o izquierda
        self.x += (self.defSettings.dspfleetUFO *
                    self.defSettings.dirfleetUFO)
        self.rect.x = self.x
