from modules.visuales import *
from modules.utilidades import guardar_puntaje
import random
import time

class Juego:
    def __init__(self, preguntas: list, menu_select: pygame.mixer.Sound, pickup_coin: pygame.mixer.Sound, game_over: pygame.mixer.Sound) -> None:
        """
        Inicializa una instancia de Juego con las preguntas y sonidos necesarios.

        Args:
            preguntas (list): Lista de preguntas para el juego.
            menu_select (pygame.mixer.Sound): Sonido para la selección en el menú.
            pickup_coin (pygame.mixer.Sound): Sonido para recolección de moneda.
            game_over (pygame.mixer.Sound): Sonido para fin de juego.
        """
        self.estados = {
            "inicio": True,
            "nombre": False,
            "preguntas": False,
            "siguiente": False,
            "reiniciar": False
        }

        self.preguntas = preguntas
        self.puntaje = 0
        self.pregunta_actual = 0
        self.comodines = {"Next": 1, "Half": 1, "Reload": 1}
        self.nombre = ""

        self.tiempo_inicio = 0
        self.tiempo_maximo = 15
        self.tiempo_restante = self.tiempo_maximo

        self.votantes = []
        self.cantidad_opcion_uno = 0
        self.cantidad_opcion_dos = 0
        self.respuesta_correcta = ""

        self.menu_select = menu_select
        self.pickup_coin = pickup_coin
        self.game_over = game_over

    def dibujar_pantallas(self, pantalla: pygame.Surface, fuente: pygame.font.Font) -> None:
        """
        Dibuja la pantalla actual del juego según el estado actual.

        Args:
            pantalla (pygame.Surface): Superficie de Pygame donde se dibujará.
            fuente (pygame.font.Font): Fuente utilizada para renderizar texto.
        """
        if self.estados["inicio"]:
            dibujar_inicio(pantalla, fuente)
        elif self.estados["nombre"]:
            escribir_nombre(pantalla, fuente, self.nombre)
        elif self.estados["preguntas"]:
            calcular_tiempo_restante = lambda inicio, maximo: maximo - (time.time() - inicio)
            self.tiempo_restante = calcular_tiempo_restante(self.tiempo_inicio, self.tiempo_maximo)
            if self.tiempo_restante <= 0:
                self.cambiar_pantalla("preguntas", "reiniciar")
            dibujar_cuadro(pantalla, fuente, self.preguntas[self.pregunta_actual])
            dibujar_votantes(pantalla)
            dibujar_tiempo(pantalla, fuente, self.tiempo_restante)
            dibujar_comodines(pantalla, fuente, self.comodines)
            dibujar_puntaje(pantalla, fuente, self.puntaje)
        elif self.estados["siguiente"]:
            pintar_votantes(pantalla, self.votantes)
            dibujar_boton_texto(pantalla, fuente, "SEGUIR")
        elif self.estados["reiniciar"]:
            dibujar_final(pantalla, fuente, self.nombre, self.puntaje, self.votantes)

    def cambiar_pantalla(self, cambiar_de: str, cambiar_a: str) -> None:
        """
        Cambia el estado de la pantalla de un estado a otro.

        Args:
            cambiar_de (str): Estado actual que se cambiará.
            cambiar_a (str): Nuevo estado al que se cambiará.
        """
        self.estados[cambiar_de] = False
        self.estados[cambiar_a] = True

    def ejecutar_eventos(self, x: int, y: int) -> None:
        """
        Ejecuta acciones según la interacción del usuario en la pantalla actual.

        Args:
            x (int): Coordenada x del clic del usuario.
            y (int): Coordenada y del clic del usuario.
        """
        if self.estados["inicio"]:
            if x >= 318 and x <= 520 and y >= 487 and y <= 565:
                self.menu_select.play()
                self.cambiar_pantalla("inicio", "nombre")
        elif self.estados["nombre"] and self.nombre:
            if x >= 318 and x <= 520 and y >= 487 and y <= 565:
                self.menu_select.play()
                self.tiempo_inicio = time.time()
                self.cambiar_pantalla("nombre", "preguntas")
                self.generar_votos_aleatorios()
                self.contar_votos()
                self.determinar_respuesta_correcta()
        elif self.estados["preguntas"]:
            self.eventos_preguntas(x, y)
        elif self.estados["siguiente"]:
            if x >= 318 and x <= 520 and y >= 487 and y <= 565:
                self.menu_select.play()
                self.generar_votos_aleatorios()
                self.contar_votos()
                self.determinar_respuesta_correcta()
                self.tiempo_inicio = time.time()
                self.cambiar_pantalla("siguiente", "preguntas")
        elif self.estados["reiniciar"]:
            if x >= 318 and x <= 520 and y >= 487 and y <= 565:
                self.menu_select.play()
                guardar_puntaje("data/puntajes.csv", self.nombre, self.puntaje)
                self.nombre = ""
                self.puntaje = 0
                self.pregunta_actual = 0
                self.tiempo_inicio = time.time()
                for comodin in self.comodines.keys():
                    self.comodines[comodin] = 1
                self.cambiar_pantalla("reiniciar", "inicio")

    def presionar_opciones(self, x: int, y: int) -> str | None:
        """
        Determina la opción seleccionada por el jugador durante las preguntas.

        Args:
            x (int): Coordenada x del clic del jugador.
            y (int): Coordenada y del clic del jugador.

        Returns:
            str | None: Devuelve "Rojo" si se selecciona la opción roja, "Azul" si se selecciona la opción azul, None si no se selecciona ninguna opción.
        """
        if 190 <= x <= 380 and 225 <= y <= 320:
            jugador_eleccion = "Rojo"
        elif 420 <= x <= 610 and 225 <= y <= 320:
            jugador_eleccion = "Azul"
        else:
            jugador_eleccion = None
        return jugador_eleccion
    
    def presionar_comodines(self, x: int, y: int) -> str | None:
        """
        Determina el comodín seleccionado por el jugador durante las preguntas.

        Args:
            x (int): Coordenada x del clic del jugador.
            y (int): Coordenada y del clic del jugador.

        Returns:
            str | None: Devuelve el nombre del comodín seleccionado ("Next", "Half", "Reload") o None si no se selecciona ningún comodín.
        """
        if x >= 190 and x <= 250 and y >= 345 and y <= 405:
            comodin_eleccion = "Next"
        elif x >= 290 and x <= 350 and y >= 345 and y <= 405:
            comodin_eleccion = "Half"
        elif x >= 390 and x <= 450 and y >= 345 and y <= 405:
            comodin_eleccion = "Reload"
        else:
            comodin_eleccion = None
        return comodin_eleccion

    def generar_votos_aleatorios(self) -> None:
        """
        Genera votos aleatorios para la pregunta actual y los guarda en la lista de votantes.
        """
        self.votantes = []

        for _ in range(5):
            voto = random.choice([VOTO_ROJO, VOTO_AZUL])
            self.votantes.append(voto)

    def contar_votos(self) -> None:
        """
        Cuenta la cantidad de votos para cada opción (Rojo y Azul) en la lista de votantes.
        """
        self.cantidad_opcion_uno = 0
        self.cantidad_opcion_dos = 0

        for voto in self.votantes:
            if voto == VOTO_ROJO:
                self.cantidad_opcion_uno += 1
            elif voto == VOTO_AZUL:
                self.cantidad_opcion_dos += 1

    def determinar_respuesta_correcta(self) -> None:
        """
        Determina cuál es la respuesta correcta basada en la cantidad de votos para cada opción.
        """
        if self.cantidad_opcion_uno > self.cantidad_opcion_dos:
            self.respuesta_correcta = "Rojo"
        else:
            self.respuesta_correcta = "Azul"

    def eventos_preguntas(self, x: int, y: int) -> None:
        """
        Maneja las interacciones del usuario durante la pantalla de preguntas.

        Args:
            x (int): Coordenada x del clic del usuario.
            y (int): Coordenada y del clic del usuario.
        """
        eleccion = self.presionar_opciones(x, y)
        if eleccion:
            if eleccion == self.respuesta_correcta:
                self.pickup_coin.play()
                self.puntaje += 1
                self.pregunta_actual += 1
                self.cambiar_pantalla("preguntas", "siguiente")
            else:
                self.game_over.play()
                self.cambiar_pantalla("preguntas", "reiniciar")

        comodin = self.presionar_comodines(x, y)
        if comodin:
            if self.comodines[comodin] == 1:
                self.menu_select.play()
                self.comodines[comodin] = 0
                if comodin == "Next":
                    self.puntaje += 1
                    self.pregunta_actual += 1
                    self.cambiar_pantalla("preguntas", "siguiente")
                elif comodin == "Half":
                    pass
                elif comodin == "Reload":
                    self.pregunta_actual += 1
