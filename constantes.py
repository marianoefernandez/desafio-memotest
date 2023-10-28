import utils

# Colores
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)
COLOR_GRIS = (206, 206, 206)
COLOR_AZUL = (30, 136, 229)
COLOR_ROJO = (255,0,0)
COLOR_VERDE = (0,255,0)

#Seteos Juego
ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480
ALTO_TEXTO = 50
TAMANIO_TEXTO = 20
CANTIDAD_TARJETAS_H = 3
CANTIDAD_TARJETAS_V = 4
CANTIDAD_TARJETAS = int((CANTIDAD_TARJETAS_H*CANTIDAD_TARJETAS_V))
CANTIDAD_TARJETAS_UNICAS = int((CANTIDAD_TARJETAS_H*CANTIDAD_TARJETAS_V)/2)
ANCHO_TARJETA = int(ANCHO_PANTALLA / CANTIDAD_TARJETAS_H)
ALTO_TARJETA =int((ALTO_PANTALLA - ALTO_TEXTO)/ CANTIDAD_TARJETAS_V)
TIEMPO_MOVIMIENTO = 3000
FPS = 60
TIEMPO_JUEGO = 30
CANTIDAD_MOVIMIENTOS = 15
CARPETA_RECURSOS = "recursos/"

# Audio
#Creo los sonidos
SONIDO_CLICK = utils.generar_sonido("{0}{1}".format(CARPETA_RECURSOS,"clic.wav"), 0.1)
SONIDO_ERROR = utils.generar_sonido("{0}{1}".format(CARPETA_RECURSOS,"equivocado.wav"), 0.1)
SONIDO_ACIERTO = utils.generar_sonido("{0}{1}".format(CARPETA_RECURSOS,"acierto.wav"), 0.1)
SONIDO_VOLTEAR = utils.generar_sonido("{0}{1}".format(CARPETA_RECURSOS,"voltear.wav"), 0.25)

utils.generar_musica("{0}{1}".format(CARPETA_RECURSOS,"fondo.wav"),0.1)#Genero la música de fondo


