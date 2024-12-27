import time
from pynput.keyboard import Controller, Key

# Inicializamos el controlador del teclado
keyboard = Controller()

# Tiempo entre cada salto en segundos
tiempo_entre_saltos = 0.5  # Ajusta el intervalo según prefieras

print("Presiona Ctrl+C para detener el script.")

try:
    while True:
        # Simula presionar y soltar la flecha hacia arriba
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        # Pausa antes del próximo salto
        time.sleep(tiempo_entre_saltos)
except KeyboardInterrupt:
    print("Script detenido.")
