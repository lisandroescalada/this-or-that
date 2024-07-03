import random

class Juego:
    def __init__(self) -> None:
        self.inicio = True
        self.preguntas = False
        self.siguiente = False
        self.reiniciar = False
        self.tiempo = False

        self.votantes = []
        self.cantidad_opcion_uno = 0
        self.cantidad_opcion_dos = 0

        self.pregunta_actual = 0
        self.comodines_usados = {"Next": 1, "Half": 1, "Reload": 1}

    def presionar_inicio(self, x: int, y: int) -> None:
        if x >= 218 and x <= 380 and y >= 485 and y <= 565:
            self.inicio = False
            self.preguntas = True
            self.tiempo = True

    def presionar_opciones(self, x: int, y: int) -> str|None:
        if x >= 190 and x <= 380 and y >= 220 and y <= 310:
            jugador_eleccion = "Rojo"
        elif x >= 420 and x <= 610 and y >= 220 and y <= 310:
            jugador_eleccion = "Azul"
        else:
            jugador_eleccion = None
        return jugador_eleccion

    def presionar_comodines(self, x: int, y: int) -> str|None:
        if x >= 190 and x <= 250 and y >= 340 and y <= 400:
            comodin_eleccion = "Next"
        elif x >= 290 and x <= 350 and y >= 340 and y <= 400:
            comodin_eleccion = "Half"
        elif x >= 390 and x <= 450 and y >= 340 and y <= 400:
            comodin_eleccion = "Reload"
        else:
            comodin_eleccion = None
        return comodin_eleccion

    def presionar_boton(self, x: int, y: int) -> bool:
        return x >= 318 and x <= 480 and y >= 225 and y <= 300

    def validar_eleccion(self, jugador_eleccion: str, eleccion_correcta: str) -> bool:
        return jugador_eleccion == eleccion_correcta

    def obtener_votos(self) -> None:
        self.votantes = []
        for _ in range(5):
            voto = random.choice(["Images\\voto_rojo.png", "Images\\voto_azul.png"])
            self.votantes.append(voto)

    def obtener_cantidad_votos(self) -> None:
        self.cantidad_opcion_uno = 0
        self.cantidad_opcion_dos = 0
        for voto in self.votantes:
            if voto == "Images\\voto_rojo.png":
                self.cantidad_opcion_uno += 1
            else:
                self.cantidad_opcion_dos += 1

    def obtener_respuesta_correcta(self) -> str:
        if self.cantidad_opcion_uno > self.cantidad_opcion_dos:
            eleccion_correcta = "Rojo"
        else:
            eleccion_correcta = "Azul"
        return eleccion_correcta
