from Modules.manejo_datos import *
from Modules.juego_logica import *
from Modules.visuales import *
import time

pygame.init()

pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("¿Esto o Aquello?")
fuente = pygame.font.Font("Font\\Minecraft.ttf", 28)
preguntas = cargar_preguntas("Data\\preguntas.json")
juego = Juego()

tiempo_inicio = time.time()
tiempo_maximo = 15

#sonidos
pygame.mixer.music.load('audio/musica.mp3')
pygame.mixer.music.play()

moneda = pygame.mixer.Sound('audio/moneda.mp3')
game_over = pygame.mixer.Sound('audio/game_over.mp3')


correr = True
while correr:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            correr = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos

            if juego.inicio:
                juego.presionar_inicio(x, y)

            elif juego.preguntas:
                jugador_eleccion = juego.presionar_opciones(x, y)
                comodin_eleccion = juego.presionar_comodines(x, y)

                juego.obtener_votos()
                juego.obtener_cantidad_votos()
                eleccion_correcta = juego.obtener_respuesta_correcta()

                if jugador_eleccion:
                    juego.preguntas = False
                    juego.tiempo = False
                    if juego.validar_eleccion(jugador_eleccion, eleccion_correcta):
                        pintar_votantes(pantalla, juego.votantes)
                        dibujar_boton(pantalla, fuente, "SEGUIR", (300, 300), (300, 30), (345, 255))
                        juego.siguiente = True
                    else:
                        pygame.mixer.music.stop()
                        game_over.play()
                        pintar_votantes(pantalla, juego.votantes)
                        dibujar_boton(pantalla, fuente, "VOLVER", (300, 300), (300, 30), (340, 255))
                        juego.reiniciar = True

                elif comodin_eleccion:
                    if juego.comodines_usados[comodin_eleccion] == 1:
                        juego.comodines_usados[comodin_eleccion] = 0
                        if comodin_eleccion == "Next":
                            juego.preguntas = False
                            juego.tiempo = False
                            pintar_votantes(pantalla, juego.votantes)
                            dibujar_boton(pantalla, fuente, "SEGUIR", (300, 300), (300, 30), (345, 255))
                            juego.siguiente = True
                        elif comodin_eleccion == "Half":
                            pass
                        elif comodin_eleccion == "Reload":
                            juego.pregunta_actual += 1

            elif juego.siguiente:
                if juego.presionar_boton(x, y):
                    tiempo_inicio = time.time()
                    juego.pregunta_actual += 1
                    juego.puntuacion += 1
                    if juego.puntuacion:
                        moneda.play()
                    juego.siguiente = False
                    juego.preguntas = True
                    juego.tiempo = True

            elif juego.reiniciar:
                # pygame.mixer.music.stop()
                # game_over.play()
                if juego.presionar_boton(x, y):
                    tiempo_inicio = time.time()
                    game_over.stop()
                    pygame.mixer.music.play()
                    tiempo_inicio = time.time()
                    juego.pregunta_actual = 0
                    juego.puntuacion = 0
                    for comodin in juego.comodines_usados.keys():
                        juego.comodines_usados[comodin] = 1
                    juego.reiniciar = False
                    juego.inicio = True

    if juego.tiempo:
        tiempo_restante = tiempo_maximo - (time.time() - tiempo_inicio)
        if tiempo_restante <= 0:
            juego.preguntas = False
            dibujar_boton(pantalla, fuente, "VOLVER", (300, 300), (300, 30), (340, 255))
            juego.reiniciar = True

    if juego.inicio:
        dibujar_inicio(pantalla, fuente)
    elif juego.preguntas:
        if juego.pregunta_actual < len(preguntas):
            dibujar_preguntas(pantalla, fuente, preguntas[juego.pregunta_actual], juego.puntuacion, juego.comodines_usados, tiempo_restante)

    pygame.display.update()

pygame.quit()