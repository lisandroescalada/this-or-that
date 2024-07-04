from modules.utilidades import *
from modules.visuales import *
from modules.juego import Juego

pygame.init()
pygame.mixer.init()

logo = pygame.image.load("assets/images/logo.png")
pantalla = pygame.display.set_mode((800, 600))
fuente = pygame.font.Font("assets/fonts/VT323.ttf", 40)

pygame.display.set_caption("¿Esto o Aquello?")
pygame.display.set_icon(logo)

preguntas = cargar_preguntas("data/preguntas.json")

soundtrack = cargar_sonido("assets/sounds/Soundtrack.mp3", 0.2)
menu_select = cargar_sonido("assets/sounds/Menu_Select.wav", 0.1)
pickup_coin = cargar_sonido("assets/sounds/Pickup_Coin.wav", 0.1)
game_over = cargar_sonido("assets/sounds/Game_Over.wav", 0.1)

juego = Juego(preguntas, menu_select, pickup_coin, game_over)

soundtrack.play()

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            juego.ejecutar_eventos(x, y)

        if juego.estados["nombre"]:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    juego.nombre = juego.nombre[:-1]
                else:
                    if len(juego.nombre) < 9:
                        juego.nombre += evento.unicode

    juego.dibujar_pantallas(pantalla, fuente)

    pygame.display.update()

pygame.quit()