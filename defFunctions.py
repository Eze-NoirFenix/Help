# Funcion de eventos facilita la lectura del codigo
import sys
import pygame
from shipBullets import Canon
from defUFO import ufoShip

def chkDOWN(defMoves, defSettings, Image, sttShip, defCanon):  # responde a cuando se presciona las keys
            if defMoves.key == pygame.K_RIGHT:  # activa movimientos a la derecha
                sttShip.rMove = True  # actualizacion de movimientos desde otro archivo
            elif defMoves.key == pygame.K_LEFT:
                sttShip.lMove = True
            elif defMoves.key == pygame.K_SPACE:
                canonShot(defSettings, Image, sttShip, defCanon)
            elif defMoves.key == pygame.K_q:  #.key porque se basa en una tecla no un evento
                sys.exit()

def chkUP(defMoves, sttShip):  # responde cuando las teclas se sueltan
            if defMoves.key == pygame.K_RIGHT:
                sttShip.rMove = False
            elif defMoves.key == pygame.K_LEFT:
                sttShip.lMove = False

def chkEvent (defSettings, Image, sttShip, defCanon):  # registra los eventos del teclado y mouse
    for defMoves in pygame.event.get():  # da permiso a defMoves
        if defMoves.type == pygame.KEYDOWN:
            chkDOWN(defMoves, defSettings, Image, sttShip, defCanon)
        elif defMoves.type == pygame.KEYUP:
            chkUP(defMoves, sttShip)

# Reescribe en el marco cada vuelta de loop y define el color desde otro archivo
def scrUpdate (defSettings, Image, sttShip, enemyUFOs, defCanon):
    Image.fill(defSettings.rgbColor)  # rellena con fill a Image
    for shipBullets in defCanon.sprites():  # dibuja los disparos
       shipBullets.imgBullet()
    sttShip.blitme()   # origina la nave sobre el fondo
    enemyUFOs.draw(Image)  # origina el enemigo

    pygame.display.flip()  # hace los dibujos visibles en pantalla

def canonShot (defSettings, Image, sttShip, defCanon):  # acciona disparo hasta su limite
   if len(defCanon) < defSettings.maxBullet:
                    shCanon = Canon(defSettings, Image, sttShip)
                    defCanon.add(shCanon)  # crea un nuevo bullet y lo agrega al grupo

def fireUpdate (defCanon):  # actualiza los disparos
    defCanon.update()

     # Se deshace de viejos disparos
    for shipBullets in defCanon.copy():
        if shipBullets.rect.bottom <= 0:
            defCanon.remove(shipBullets)
    print (len(defCanon))


def getnumUFOx(defSettings, widUFO):
    # determina la cantidad de enemigos en linea
    disSpaceX = defSettings.widImage - 2 * widUFO
    numUFOX = int(disSpaceX / (2 * widUFO))
    return numUFOX

def getnumWaves(defSettings, heiShip, heiUFO):
    # determina cuantas waves caben en pantalla
    disSpaceY = (defSettings.heiImage - (3 * heiUFO) - heiShip)
    numWaves = int(disSpaceY / (2 * heiUFO))  # cuantas veces se multiplica la flota
    return numWaves

def createUFO(defSettings, Image, enemyUFOs, numUFO, numWave):
    # crea al enemigo y lo coloca en la fila
    defUFO = ufoShip(defSettings, Image)
    widUFO = defUFO.rect.width
    defUFO.x = widUFO + 2 * widUFO * numUFO  # separacion horizontal
    defUFO.rect.x = defUFO.x
    defUFO.rect.y = defUFO.rect.height + 2 * defUFO.rect.height * numWave  # vertical
    enemyUFOs.add(defUFO)

def ufoFleet(defSettings, Image, sttShip, enemyUFOs):
    # crea la flota de aliens
    # calculo que indica cuantos caben en pantalla
    defUFO = ufoShip(defSettings, Image)
    numUFOX = getnumUFOx(defSettings, defUFO.rect.width)
    numWaves = getnumWaves(defSettings, sttShip.rect.height,
        defUFO.rect.height)

    # crea la primera linea de aliens
    for numWave in range (numWaves):
        for numUFO in range (numUFOX):
            createUFO(defSettings, Image, enemyUFOs, numUFO,
                numWave)

def chkfleetEdge(defSettings, enemyUFOs):
    # responde cuando el enemig llega al borde
    for defUFO in enemyUFOs.sprites():
        if defUFO.chkEdge():
            TdirfleetUFO(defSettings, enemyUFOs)
            break

def TdirfleetUFO(defSettings, enemyUFOs):
    # baja la flota entera
    for defUFO in enemyUFOs.sprites():
        defUFO.rect.y += defSettings.dspfleetUFO
    defSettings.dirfleetUFO *= -1

def updateUFO(defSettings, enemyUFOs):
    # se fija si esta la flota al borde
    chkfleetEdge(defSettings, enemyUFOs)
    # actualiza los movimientos del enemigo
    enemyUFOs.update()

