import pygame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (50, 130, 200)

def dibujar_texto(pantalla, fuente, texto: str, color: tuple, posicion: tuple) -> None:
    texto = fuente.render(texto, True, color)
    pantalla.blit(texto, posicion)

def dibujar_imagen(pantalla, path: str, resolucion: tuple, posicion: tuple) -> None:
    imagen = pygame.image.load(path)
    imagen_escala = pygame.transform.scale(imagen, resolucion)
    pantalla.blit(imagen_escala, posicion)

def dibujar_preguntas(pantalla, fuente, pregunta: dict, puntaje: int) -> None:
    pantalla.fill(AZUL)
    dibujar_imagen(pantalla, "Img\\cuadro.jpg", (500, 500), (50, 0))
    dibujar_texto(pantalla, fuente, pregunta["pregunta"], NEGRO, (130, 160))

    dibujar_imagen(pantalla, "Img\\boton_rojo.jpg", (250, 250), (120, 50))
    dibujar_texto(pantalla, fuente, pregunta["opciones"][0], BLANCO, (165, 230))

    dibujar_imagen(pantalla, "Img\\boton_azul.jpg", (250, 250), (310, 50))
    dibujar_texto(pantalla, fuente, pregunta["opciones"][1], BLANCO, (365, 230))

    dibujar_imagen(pantalla, "Img\\moneda.jpg", (50, 50), (510, 7))
    dibujar_texto(pantalla, fuente, f"{puntaje}", BLANCO, (560, 15))

    dibujar_imagen(pantalla, "Img\\voto_neutro.jpg", (400, 400), (-100, 195))
    dibujar_imagen(pantalla, "Img\\voto_neutro.jpg", (400, 400), (0, 195))
    dibujar_imagen(pantalla, "Img\\voto_neutro.jpg", (400, 400), (100, 195))
    dibujar_imagen(pantalla, "Img\\voto_neutro.jpg", (400, 400), (200, 195))
    dibujar_imagen(pantalla, "Img\\voto_neutro.jpg", (400, 400), (300, 195))

    # dibujar_imagen(pantalla, "Img\\next.jpg", (250, 250), (5, 355))
    # dibujar_imagen(pantalla, "Img\\half.jpg", (250, 250), (105, 355))
    # dibujar_imagen(pantalla, "Img\\reload.jpg", (250, 250), (205, 355))

def dibujar_final(pantalla, fuente, puntaje: int) -> None:
    pantalla.fill(NEGRO)
    dibujar_texto(pantalla, fuente, f"FIN DEL JUEGO. Puntaje: {puntaje}", BLANCO, (100, 200))

def dibujar_boton(pantalla, fuente):
    dibujar_imagen(pantalla, "Img\\boton_siguiente.jpg", (250, 250), (430, 355))
    dibujar_texto(pantalla, fuente, "Seguir", BLANCO, (466, 532))

def votantes_eleccion(pantalla, lista_votos: list) -> None:
    dibujar_imagen(pantalla, lista_votos[0], (400, 400), (-100, 195))
    dibujar_imagen(pantalla, lista_votos[1], (400, 400), (0, 195))
    dibujar_imagen(pantalla, lista_votos[2], (400, 400), (100, 195))
    dibujar_imagen(pantalla, lista_votos[3], (400, 400), (200, 195))
    dibujar_imagen(pantalla, lista_votos[4], (400, 400), (300, 195))