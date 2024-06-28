import random
import time
from ui import dibujar_final

def validar_eleccion(x: int, y: int) -> str|None:
    if x >= 135 and x <= 270 and y >= 215 and y <= 280:
        jugador_eleccion = "Rojo"
    elif x >= 325 and x <= 460 and y >= 215 and y <= 280:
        jugador_eleccion = "Azul"
    else:
        jugador_eleccion = None

    return jugador_eleccion

def validar_eleccion_correcta(jugador_eleccion: str, eleccion_correcta: str) -> bool:
    return jugador_eleccion == eleccion_correcta

def obtener_votos() -> list:
    lista_votos = []

    for _ in range(5):
        voto = random.choice(["Img\\voto_rojo.jpg", "Img\\voto_azul.jpg"])
        lista_votos.append(voto)

    return lista_votos

def obtener_cantidad_votos(lista_votos: list) -> int:
    primera_opcion = 0
    segunda_opcion = 0

    for voto in lista_votos:
        if voto == "Img\\voto_rojo.jpg":
            primera_opcion += 1
        else:
            segunda_opcion += 1

    return primera_opcion, segunda_opcion

def obtener_respuesta_correcta(primera_opcion: int, segunda_opcion: int) -> str:
    if primera_opcion > segunda_opcion:
        respuesa_correcta = "Rojo"
    else:
        respuesa_correcta = "Azul"

    return respuesa_correcta

def siguiente_nivel(x: int, y: int) -> bool:
    return x >= 445 and x <= 580 and y >= 515 and y <= 575

def comodin_next(x: int, y: int) -> bool:
    return x >= 5 and x <= 255 and y >= 355 and y <= 605
    
    
    

