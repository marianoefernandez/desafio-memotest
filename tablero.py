from constantes import *

def crear_tablero():
    '''
    Crea un diccionario con toda la informacion necesaria para el tablero, creando la lista de tarjetas y todos sus parametros.
    Retorna un diccionario con el tablero
    '''
    #Creo el diccionario del tablero 
    pass

def generar_lista_tarjetas()->list:
    '''
    Función que se encarga de generar una lista de tarjetas.
    Va a generar la cantidad de tarjetas que le especifique anteriormente con las constantes teniendo en cuenta el eje X y el eje Y correspondiente de las superficies de cada una de las tarjetas.
    Retorna la lista de las tarjetas generadas
    '''
    lista_tarjetas = []
    indice = 0
    lista_id = generar_lista_ids_tarjetas() 
    
    #Guardo cada una de las tarjetas (Tener en cuenta la posicion X e Y de las mismas)
    pass

def generar_lista_ids_tarjetas():
    '''
    Funcion que se encarga de ordenar de forma aleatoria los id de las tarjetas para que las mismas tengan un orden aleatorio en cada partida.
    '''
    #Creo la lista con los id de todas las tarjetas que voy a jugar
    #Ordeno aleatoriamente los id de las mismas
    pass
    

def detectar_colision(tablero,pos_xy):
    '''
    verifica si existe una colision alguna tarjetas del tablero y la coordenada recibida como parametro
    Recibe como parametro el tablero y una tupla (X,Y)
    Retorna el identificador de la tarjeta que colisiono con el mouse y sino retorna None
    '''
    #Manejo de colisiones
    pass

def actualizar_tablero(tablero):
    '''
    Verifica si es necesario actualizar el estado de alguna tarjeta, en funcion de su propio estado y el de las otras
    Recibe como parametro el tablero
    '''
    #Actualiza el tablero en tiempo real mientras se juega
    pass

def descubrir_tarjetas(lista_tarjetas, identificador):
    '''
        Función que se encarga de cambiarle la bandera a las tarjetas a las que el usuario haya acertado en el memotest y por ende mostrarlas.
        Recorre las tarjetas de la lista y si tiene el mismo identificador que el pasado por parametro y tambien la misma no ha sido descubierta anteriormente cambia la bandera de la clave descubierto a True
        Recibe la lista de tarjetas y el identificador a la que le va a reemplazar la bandera descubierto
    '''
    #Cambio la bandera de desubierto a True si la misma no se descubrio anteriormente.
    pass

def comparar_tarjetas(tablero):
    '''
    Funcion que se encarga de encontrar un match en la selección de las tarjetas del usuario.
    Si el usuario selecciono dos tarjetas está función se encargara de verificar si el identificador 
    de las mismas corresponde si es así retorna True, sino False. 
    En caso de que no hayan dos tarjetas seleccionadas retorna None
    '''
    #Verifico si las tarjetas seleccionadas por el jugador coinciden o no (Llamar a la funcion de arriba descubrir_tarjetas si hay match)
    pass

def dibujar_tablero(tablero,pantalla_juego):
    '''
    Dibuja todos los elementos del tablero en la superficie recibida como parametro
    Recibe como parametro el tablero
    '''
    #Dibuja el tablero con todas las cartas en la pantalla de mi juego
    pass
     