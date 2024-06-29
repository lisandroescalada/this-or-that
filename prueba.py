import time
def temporizador(segundos: int) -> str:
    for cantidad in range(segundos, 0, -1):
        print(f"te quedan {cantidad} segundos")
        time.sleep(1)
    print("se terminó el tiempo")
    
temporizador(5)