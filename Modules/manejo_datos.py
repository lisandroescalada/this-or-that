import json

def cargar_preguntas(path: str) -> list:
    with open(path, "r", encoding = "utf8") as archivo:
        preguntas = json.load(archivo)
    return preguntas

def guardar_puntacion(path: str, nombre: str, puntuacion: int) -> None:
    with open(path, "a") as archivo:
        archivo.write(f"{nombre},{puntuacion}\n")
