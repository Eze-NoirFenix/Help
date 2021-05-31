#Configuracion Defender

class defenderConfig(): # crea una clase donde se almacena las configuraciones del juego
    def __init__ (self): # inicia las configuraciones del juego init es un metodo
        #configuaraciones de pantalla
        self.widImage = 1200
        self.heiImage = 800
        self.rgbColor = (1, 3, 42)

        # Bullets config
        self.speedBullet = 6
        self.widBullet = 4 # pixels
        self.heiBullet = 10
        self.rgbBullet = 250, 250, 250
        self.maxBullet = 2

        # Ship Config
        self.speedsetShip = 3.00

        # UFO Config
        self.speedsetUFO = 1
        self.dspfleetUFO = 1
        #  la representacion 1 es para la derecha -1 izquierda
        self.dirfleetUFO = 1
