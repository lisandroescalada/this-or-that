from ui import *
from game import *
from data import preguntas
import time

pygame.init()

fuente = pygame.font.Font("Font\\PixelifySans.ttf", 30)
pantalla = pygame.display.set_mode((600, 600))
pygame.display.set_caption("¿Esto o Aquello?")

tiempo_inicio = time.time()
tiempo_maximo = 15

correr = True
while correr:
    tiempo_restante = tiempo_maximo - (time.time() - tiempo_inicio)
    if tiempo_restante <= 0:
        dibujar_boton(pantalla, fuente, "Volver")
        pantalla_preguntas = False
        reiniciar = True

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            correr = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos

            if pantalla_preguntas:
                jugador_eleccion = validar_eleccion(x, y)
                comodin_eleccion = validar_comodines(x, y)

                lista_votos = obtener_votos()
                primera_opcion, segunda_opcion = obtener_cantidad_votos(lista_votos)
                eleccion_correcta = obtener_respuesta_correcta(primera_opcion, segunda_opcion)

                siguiente = False
                reiniciar = False

                if jugador_eleccion:
                    pantalla_preguntas = False
                    if validar_eleccion_correcta(jugador_eleccion, eleccion_correcta):
                        votantes_eleccion(pantalla, lista_votos)
                        dibujar_boton(pantalla, fuente, "Seguir")
                        siguiente = True
                    else:
                        votantes_eleccion(pantalla, lista_votos)
                        dibujar_boton(pantalla, fuente, "Volver")
                        reiniciar = True

                if comodin_eleccion:
                    if comodin_eleccion == "Next" and next:
                        votantes_eleccion(pantalla, lista_votos)
                        pantalla_preguntas = False
                        dibujar_boton(pantalla, fuente, "Seguir")
                        siguiente = True
                        next = False

                    elif comodin_eleccion == "Half" and half:
                        pantalla_preguntas = False
                        votantes_eleccion(pantalla, lista_votos, False)
                        half = False

                    elif comodin_eleccion == "Reload" and reload:
                        indice_pregunta += 1
                        reload = False

                    comodin_eleccion = None

            if siguiente:
                if oprimir_boton(x, y):
                    tiempo_inicio = time.time()
                    indice_pregunta += 1
                    puntaje += 1
                    pantalla_preguntas = True

            elif reiniciar:
                if oprimir_boton(x, y):
                    tiempo_inicio = time.time()
                    indice_pregunta = 0
                    puntaje = 0
                    next = True
                    reload = True
                    half = True
                    pantalla_preguntas = True

    if pantalla_preguntas:
        if indice_pregunta < len(preguntas):
            dibujar_preguntas(pantalla, fuente, preguntas[indice_pregunta], puntaje, tiempo_restante)
        else:
            # pantalla.fill(NEGRO)
            pantalla_preguntas = False
            siguiente = False
            reiniciar = False

    pygame.display.update()

pygame.quit()