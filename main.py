from ui import *
from game import *
from data import preguntas

pygame.init()

fuente = pygame.font.Font("Font\\PixelifySans.ttf", 30)
pantalla = pygame.display.set_mode((600, 600))
pygame.display.set_caption("¿Esto o Aquello?")

pantalla_preguntas = True
puntaje = 0
indice_pregunta = 0

correr = True
while correr:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            correr = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos

            if pantalla_preguntas:
                jugador_eleccion = validar_eleccion(x, y)
                lista_votos = obtener_votos()
                primera_opcion, segunda_opcion = obtener_cantidad_votos(lista_votos)
                eleccion_correcta = obtener_respuesta_correcta(primera_opcion, segunda_opcion)
                siguiente = False

                if jugador_eleccion:
                    if validar_eleccion_correcta(jugador_eleccion, eleccion_correcta):
                        dibujar_boton(pantalla, fuente)
                        puntaje += 1
                        pantalla_preguntas = False
                        siguiente = True
                    else:
                        dibujar_final(pantalla, fuente, puntaje)
                        pantalla_preguntas = False
                        siguiente = False

            if siguiente:
                votantes_eleccion(pantalla, lista_votos)
                if siguiente_nivel(x, y):
                    indice_pregunta += 1
                    pantalla_preguntas = True

    if pantalla_preguntas:
        if indice_pregunta < len(preguntas):
            dibujar_preguntas(pantalla, fuente, preguntas[indice_pregunta], puntaje)
        else:
            dibujar_final(pantalla, fuente, puntaje)
            pantalla_preguntas = False
            siguiente = False

    pygame.display.update()

pygame.quit()