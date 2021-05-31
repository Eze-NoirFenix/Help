# Defender
import pygame
from pygame.sprite import Group
from defCONFIG import defenderConfig  # importa el nuevo archivo creado
from defShip import defenderShip  # importa el archivo de la nave
import defFunctions as df

def startGame():  # El siguiente codigo iniciará el juego, configuraciones y objetos en pantalla
    pygame.init()  # inicializa las configuacines necesarias para Pygame
    defSettings = defenderConfig()  # almanecena el otro archivo en  este codigo
    # la siguiente linea crea el marco en pantalla proveniente de otro archivo
    Image = pygame.display.set_mode((defSettings.widImage, defSettings.heiImage))
    pygame.display.set_caption('Defender')

    # importa la nave antes del loop asi no lo hace a cada rato
    # UPDATE! (screen) por (defSettings)
    sttShip = defenderShip(defSettings, Image)
    # importa el grupo de canon
    defCanon = Group()
    # importa el grupo de enemigo
    enemyUFOs = Group()
    # crea una flota de enemigos
    df.ufoFleet(defSettings, Image, sttShip, enemyUFOs)

    while True:  # Crea el loop para los eventos en el juego
        df.chkEvent(defSettings, Image, sttShip, defCanon)  #  codigo trasladado a diferente archivo por mejora
        sttShip.update()
        df.fireUpdate(defCanon)
        df.updateUFO(defSettings, enemyUFOs)
        df.scrUpdate(defSettings, Image, sttShip, enemyUFOs, defCanon)  #  codigo trasladado a diferente archivo por mejora



startGame()  # Inicia la funcion del codigo por ende el juego
