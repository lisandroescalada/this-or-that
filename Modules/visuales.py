import pygame

BLANCO = (255, 255, 255)
AZUL = (50, 130, 200)
NEGRO = (0, 0, 0)

IMG_TITULO = "Images/titulo.png"
IMG_CUADRO = "Images/cuadro.png"
IMG_BOTON = "Images/boton.png"
IMG_BOTON_ROJO = "Images/boton_rojo.png"
IMG_BOTON_AZUL = "Images/boton_azul.png"
IMG_NEXT = "Images/next.png"
IMG_HALF = "Images/half.png"
IMG_RELOAD = "Images/reload.png"
IMG_VOTO_NEUTRO = "Images/voto_neutro.png"
IMG_MONEDA = "Images/moneda.png"
IMG_BARRA = "Images/barra.png"

def cargar_sonido(path, volumen: float):
    sonido = pygame.mixer.Sound(path)
    sonido.set_volume(volumen)
    return sonido

def dibujar_imagen(pantalla, path: str, resolucion: tuple, posicion: tuple) -> None:
    imagen = pygame.image.load(path)
    imagen_escala = pygame.transform.scale(imagen, resolucion)
    pantalla.blit(imagen_escala, posicion)

def dibujar_texto(pantalla, fuente, texto: str, color: tuple, posicion: tuple) -> None:
    texto_superficie = fuente.render(texto, True, color)
    pantalla.blit(texto_superficie, posicion)

def dibujar_inicio(pantalla, fuente) -> None:
    pantalla.fill(AZUL)
    dibujar_boton(pantalla, fuente, "INICIO", (300, 300), (200, 290), (250, 515))
    dibujar_boton(pantalla, fuente, "PUNTOS", (300, 300), (400, 290), (445, 515))
    dibujar_imagen(pantalla, IMG_TITULO, (540, 540), (125, 0))

def dibujar_preguntas(pantalla, fuente, pregunta: str, puntuacion: int, comodines_usados: dict, tiempo_restante: int) -> None:
    pantalla.fill(AZUL)

    dibujar_imagen(pantalla, IMG_CUADRO, (600, 600), (105, -17))
    dibujar_texto(pantalla, fuente, pregunta["pregunta"], NEGRO, (200, 170))

    dibujar_imagen(pantalla, IMG_BOTON_ROJO, (350, 350), (170, -10))
    dibujar_texto(pantalla, fuente, pregunta["opciones"][0], BLANCO, (230, 255))

    dibujar_imagen(pantalla, IMG_BOTON_AZUL, (350, 350), (400, -10))
    dibujar_texto(pantalla, fuente, pregunta["opciones"][1], BLANCO, (460, 255))

    posiciones_votantes = [(-75, 230), (50, 230), (175, 230), (300, 230), (425, 230)]
    posiciones_votantes_set = set(posiciones_votantes)
    for posicion in posiciones_votantes_set:
        dibujar_imagen(pantalla, IMG_VOTO_NEUTRO, (450, 450), posicion)

    dibujar_imagen(pantalla, IMG_MONEDA, (50, 50), (705, 14))
    dibujar_texto(pantalla, fuente, f"{puntuacion}", BLANCO, (755, 30))

    dibujar_imagen(pantalla, IMG_NEXT,(300, 300), (70, 215))
    dibujar_texto(pantalla, fuente, f"{comodines_usados["Next"]}", BLANCO, (243.5, 327))

    dibujar_imagen(pantalla, IMG_HALF, (300, 300),(170, 215))
    dibujar_texto(pantalla, fuente, f"{comodines_usados["Half"]}", BLANCO, (343.5, 327))

    dibujar_imagen(pantalla, IMG_RELOAD,(300, 300), (270, 215))
    dibujar_texto(pantalla, fuente, f"{comodines_usados["Reload"]}", BLANCO, (443.5, 327))

    dibujar_imagen(pantalla, IMG_BARRA,(350, 350), (0, -260))
    dibujar_texto(pantalla, fuente, f"Tiempo Restante: {tiempo_restante:.0f}", BLANCO, (37, 37))

def dibujar_boton(pantalla, fuente, texto: str, resolucion: tuple, posicion: tuple, posicion_texto: tuple) -> None:
    dibujar_imagen(pantalla, IMG_CUADRO, (600, 600), (105, -17))
    dibujar_imagen(pantalla, IMG_BOTON, resolucion, posicion)
    dibujar_texto(pantalla, fuente, texto, BLANCO, posicion_texto)

def pintar_votantes(pantalla, lista_votos: list) -> None:
    posiciones_votantes = [
        [(-75, 230), (50, 230), (175, 230)],
        [(300, 230), (425, 230)]
    ]

    voto_index = 0
    for fila in posiciones_votantes:
        for posicion in fila:
            if voto_index < len(lista_votos):
                voto = lista_votos[voto_index]
                dibujar_imagen(pantalla, voto, (450, 450), posicion)
                voto_index += 1

def dibujar_final(pantalla, fuente, puntuacion: int) -> None:
    pantalla.fill(AZUL)
    dibujar_boton(pantalla, fuente, "VOLVER", (300, 300), (300, 40), (340, 265))
    dibujar_texto(pantalla, fuente, f"Fin del Juego. Puntaje: {puntuacion}", NEGRO, (200, 190))

def dibujar_tabla_puntos(pantalla, fuente, puntuaciones: str) -> None:
    pantalla.fill(AZUL)
    dibujar_boton(pantalla, fuente, "VOLVER", (300, 300), (300, 40), (340, 265))
    dibujar_texto(pantalla, fuente, f"{puntuaciones}\n", NEGRO, (180, 170))