# Configuaracion de la nave
import pygame

class defenderShip():

    # inicia la imagen de nave a su pocision
    def __init__(self, defSettings, screen):  # se agrega defSettings desde otro archivo
        self.screen = screen
        self.defSettings = defSettings

        # carga la imagen dejandola recta
        self.image = pygame.image.load('Image/DefenderShip RemakeBlue.bmp') #carpeta de archivo de imagen
        self.rect = self.image.get_rect() #cde este modo la imagen da atributos rectos
        self.scrRect = screen.get_rect()

        # da el posicionamiento de la nave desde el centro abajo de la pantalla
        self.rect.centerx = self.scrRect.centerx # se basa en el posicionamiento x
        self.rect.bottom = self.scrRect.bottom

        # Archiva la velocidad basado en decimales
        self.center = float(self.rect.centerx)  # float porque son decimales

        # flag de movimiento
        self.rMove = False  # false porque cuando se active dara True lo caul dará permiso
        self.lMove = False


    def update (self):  # actualiza el movimiento de la nave con flags update es un metodo
        # actualizacion sobre moviento ahora decimales (otro archivo) no recto (+= 1)
        if self.rMove and self.rect.right < self.scrRect.right:  # cuando sea menor a dara el limite
            self.center += self.defSettings.speedsetShip
        if self.lMove and self.rect.left > 0:
            self.center -= self.defSettings.speedsetShip

        # actualiza el objeto desde self.center
        self.rect.centerx = self.center

    def blitme(self):
        # dibuja la nave en la ubicacion actual
        self.screen.blit(self.image, self.rect)# metodo blitme() el cual dibujara la imagen donde rect indique
