import json

def cargar_preguntas(path: str) -> list:
    with open(path, "r", encoding = "utf8") as archivo:
        preguntas = json.load(archivo)
    return preguntas

def guardar_puntacion(path: str, puntuacion: int, jugador_num: int) -> int:
    with open(path, "a") as archivo:
        archivo.write(f"Jugador {jugador_num}: {puntuacion}\n")
        jugador_num += 1
        return jugador_num
    
def cargar_puntacion(path: str) -> str:
    puntaciones = ""
    with open(path, "r") as archivo:
        for linea in archivo:
            puntaciones += linea
    return puntaciones