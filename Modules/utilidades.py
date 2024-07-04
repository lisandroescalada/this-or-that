import pygame
import json

def cargar_preguntas(path: str) -> list[dict]:
    """
    Carga preguntas desde un archivo JSON.

    Args:
        path (str): La ruta del archivo JSON.

    Returns:
        list[dict]: Una lista de diccionarios que representan las preguntas.
    """
    with open(path, "r", encoding="utf8") as archivo:
        preguntas = json.load(archivo)
    return preguntas

def guardar_puntaje(path: str, nombre: str, puntaje: int) -> None:
    """
    Guarda la puntuación en un archivo de texto.

    Args:
        path (str): La ruta del archivo de texto.
        nombre (str): El nombre del jugador.
        puntaje (int): La puntuación a guardar.
    """
    with open(path, "a", encoding="utf8") as archivo:
        archivo.write(f"{nombre},{puntaje}\n")

def cargar_sonido(path: str, volumen: float) -> pygame.mixer.Sound:
    """
    Carga un sonido desde un archivo y establece su volumen.

    Args:
        path (str): La ruta del archivo de sonido.
        volumen (float): El volumen del sonido (de 0.0 a 1.0).

    Returns:
        pygame.mixer.Sound: El objeto de sonido cargado.
    """
    sonido = pygame.mixer.Sound(path)
    sonido.set_volume(volumen)
    return sonido

def dibujar_imagen(pantalla: pygame.Surface, path: str, resolucion: tuple[int, int], posicion: tuple[int, int]) -> None:
    """
    Carga una imagen desde la ruta especificada, la escala a la resolución deseada y la dibuja en la pantalla.

    Args:
        pantalla (pygame.Surface): La superficie donde se dibujará la imagen.
        path (str): La ruta del archivo de la imagen.
        resolucion (tuple[int, int]): La resolución (ancho, alto) a la cual escalar la imagen.
        posicion (tuple[int, int]): La posición (x, y) donde dibujar la imagen en la pantalla.
    """
    imagen = pygame.image.load(path)
    imagen_escala = pygame.transform.scale(imagen, resolucion)
    pantalla.blit(imagen_escala, posicion)

def dibujar_texto(pantalla: pygame.Surface, fuente: pygame.font.Font, texto: str, color: tuple[int, int, int], posicion: tuple[int, int]) -> None:
    """
    Renderiza y dibuja texto en la superficie especificada.

    Args:
        pantalla (pygame.Surface): La superficie donde se dibujará el texto.
        fuente (pygame.font.Font): La fuente utilizada para renderizar el texto.
        texto (str): El texto a dibujar.
        color (tuple[int, int, int]): El color del texto (RGB).
        posicion (tuple[int, int]): La posición (x, y) donde dibujar el texto en la pantalla.
    """
    texto_superficie = fuente.render(texto, True, color)
    pantalla.blit(texto_superficie, posicion)
