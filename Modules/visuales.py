import pygame
from modules.utilidades import dibujar_imagen, dibujar_texto

CREMA = (250, 245, 213)
AZUL = (50, 130, 200)
NEGRO = (0, 0, 0)

TITULO = "assets/images/titulo.png"
CUADRO = "assets/images/cuadro.png"
BOTON = "assets/images/boton.png"
BOTON_ROJO = "assets/images/boton_rojo.png"
BOTON_AZUL = "assets/images/boton_azul.png"
NEXT = "assets/images/next.png"
HALF = "assets/images/half.png"
RELOAD = "assets/images/reload.png"
VOTO_NEUTRO = "assets/images/voto_neutro.png"
VOTO_ROJO = "assets/images/voto_rojo.png"
VOTO_AZUL = "assets/images/voto_azul.png"
MONEDA = "assets/images/moneda.png"
BARRA = "assets/images/barra.png"
MINI_BOTON = "assets/images/mini_boton.png"

def dibujar_inicio(pantalla: pygame.Surface, fuente: pygame.font.Font) -> None:
    """
    Dibuja la pantalla de inicio del juego.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla de Pygame.
        fuente (pygame.font.Font): La fuente utilizada para el texto.
    """
    pantalla.fill(AZUL)
    dibujar_imagen(pantalla, CUADRO, (600, 600), (105, -15))
    dibujar_imagen(pantalla, TITULO, (600, 600), (80, -20))
    dibujar_boton_texto(pantalla, fuente, "INICIO")

def dibujar_cuadro(pantalla: pygame.Surface, fuente: pygame.font.Font, pregunta: dict) -> None:
    """
    Dibuja un cuadro con la pregunta y las opciones en botones de diferentes colores.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla de Pygame.
        fuente (pygame.font.Font): La fuente utilizada para el texto.
        pregunta (dict): El diccionario que contiene la pregunta y las opciones.
    """
    pantalla.fill(AZUL)
    dibujar_imagen(pantalla, CUADRO, (600, 600), (105, -15))
    dibujar_texto(pantalla, fuente, pregunta["pregunta"], NEGRO, (195, 165))
    dibujar_imagen(pantalla, BOTON_ROJO, (350, 350), (170, -10))
    dibujar_texto(pantalla, fuente, pregunta["opciones"][0], CREMA, (220, 245))
    dibujar_imagen(pantalla, BOTON_AZUL, (350, 350), (400, -10))
    dibujar_texto(pantalla, fuente, pregunta["opciones"][1], CREMA, (450, 245))

def dibujar_comodines(pantalla: pygame.Surface, fuente: pygame.font.Font, comodines: dict) -> None:
    """
    Dibuja los comodines en la pantalla del juego.
    
    Args:
    pantalla (pygame.Surface): La superficie donde se dibujarán los elementos.
    fuente (pygame.font.Font): La fuente utilizada para el texto.
    comodines (dict): Un diccionario con los valores de los comodines.
    """
    dibujar_imagen(pantalla, NEXT, (300, 300), (70, 220))
    dibujar_texto(pantalla, fuente, f"{comodines["Next"]}", CREMA, (242, 322))
    dibujar_imagen(pantalla, HALF, (300, 300), (170, 220))
    dibujar_texto(pantalla, fuente, f"{comodines["Half"]}", CREMA, (342, 322))
    dibujar_imagen(pantalla, RELOAD, (300, 300), (270, 220))
    dibujar_texto(pantalla, fuente, f"{comodines["Reload"]}", CREMA, (442, 322))

def escribir_nombre(pantalla: pygame.Surface, fuente: pygame.font.Font, nombre: str) -> None:
    """
    Dibuja la pantalla donde el jugador puede ingresar su nombre.
    
    Args:
    pantalla (pygame.Surface): La superficie donde se dibujarán los elementos.
    fuente (pygame.font.Font): La fuente utilizada para el texto.
    nombre (str): El nombre actual ingresado por el jugador.
    """
    pantalla.fill(AZUL)
    dibujar_imagen(pantalla, BARRA, (600, 600), (90, -250))
    dibujar_texto(pantalla, fuente, f"Ingrese nombre: {nombre}", CREMA, (170, 255))
    dibujar_boton_texto(pantalla, fuente, "SEGUIR")

def dibujar_puntaje(pantalla: pygame.Surface, fuente: pygame.font.Font, puntaje: int) -> None:
    """
    Dibuja el puntaje actual del jugador en la pantalla.
    
    Args:
    pantalla (pygame.Surface): La superficie donde se dibujarán los elementos.
    fuente (pygame.font.Font): La fuente utilizada para el texto.
    puntaje (int): El puntaje actual del jugador.
    """
    dibujar_imagen(pantalla, MONEDA, (50, 50), (705, 13))
    dibujar_texto(pantalla, fuente, f"{puntaje}", CREMA, (755, 19))

def dibujar_votantes(pantalla: pygame.Surface) -> None:
    """
    Dibuja los espacios para los votantes en la pantalla.
    
    Args:
    pantalla (pygame.Surface): La superficie donde se dibujarán los elementos.
    """
    posiciones_votantes = [(19, -130), (140.25, -130), (261.5, -130), (382.75, -130), (504, -130)]
    for posicion in posiciones_votantes:
        dibujar_imagen(pantalla, VOTO_NEUTRO, (275, 275), posicion)

def dibujar_boton_texto(pantalla: pygame.Surface, fuente: pygame.font.Font, texto: str) -> None:
    """
    Dibuja un botón con texto en la pantalla.
    
    Args:
    pantalla (pygame.Surface): La superficie donde se dibujarán los elementos.
    fuente (pygame.font.Font): La fuente utilizada para el texto.
    texto (str): El texto que se mostrará en el botón.
    """
    dibujar_imagen(pantalla, BOTON, (300, 300), (300, 285))
    dibujar_texto(pantalla, fuente, texto, CREMA, (350, 500))

def pintar_votantes(pantalla: pygame.Surface, votantes: list) -> None:
    """
    Pinta los votantes en sus respectivas posiciones en la pantalla.
    
    Args:
    pantalla (pygame.Surface): La superficie donde se dibujarán los elementos.
    votantes (list): Una lista de imágenes de los votantes.
    """
    posiciones_votantes = [
        [(19, -130), (140.25, -130), (261.5, -130)],
        [(382.75, -130), (504, -130)]
    ]

    voto_index = 0
    for fila in posiciones_votantes:
        for posicion in fila:
            if voto_index < len(votantes):
                voto = votantes[voto_index]
                dibujar_imagen(pantalla, voto, (275, 275), posicion)
                voto_index += 1

def dibujar_final(pantalla: pygame.Surface, fuente: pygame.font.Font, nombre: str, puntaje: int, votantes: list) -> None:
    """
    Dibuja la pantalla final del juego con el nombre, puntaje y votantes.
    
    Args:
    pantalla (pygame.Surface): La superficie donde se dibujarán los elementos.
    fuente (pygame.font.Font): La fuente utilizada para el texto.
    nombre (str): El nombre del jugador.
    puntaje (int): El puntaje final del jugador.
    votantes (list): Una lista de imágenes de los votantes.
    """
    pantalla.fill(AZUL)
    dibujar_imagen(pantalla, CUADRO, (600, 600), (105, -15))
    dibujar_texto(pantalla, fuente, "FIN DEL JUEGO", NEGRO, (295, 170))
    dibujar_texto(pantalla, fuente, f"Nombre: {nombre}", NEGRO, (195, 210))
    dibujar_texto(pantalla, fuente, f"Puntaje: {puntaje}", NEGRO, (195, 240))
    pintar_votantes(pantalla, votantes)
    dibujar_boton_texto(pantalla, fuente, "VOLVER")

def dibujar_tiempo(pantalla: pygame.Surface, fuente: pygame.font.Font, tiempo_restante: float) -> None:
    """
    Dibuja el tiempo restante en la pantalla.

    Args:
        pantalla (pygame.Surface): La superficie donde se dibujará el tiempo.
        fuente (pygame.font.Font): La fuente utilizada para renderizar el texto.
        tiempo_restante (float): El tiempo restante en segundos.
    """
    dibujar_imagen(pantalla, MINI_BOTON, (400, 400), (-145, -144))
    tiempo_formateado = f"{tiempo_restante:02.0f}"
    dibujar_texto(pantalla, fuente, tiempo_formateado, CREMA, (43, 40))
