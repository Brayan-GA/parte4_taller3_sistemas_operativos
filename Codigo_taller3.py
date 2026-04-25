import threading
import time

# Función que ejecuta el hilo 1
def tarea1():
    for i in range(5):
        print("Hilo 1 ejecutando:", i)
        time.sleep(1)

# Función que ejecuta el hilo 2
def tarea2():
    for i in range(5):
        print("Hilo 2 ejecutando:", i)
        time.sleep(1)

# Crear los hilos
hilo1 = threading.Thread(target=tarea1)
hilo2 = threading.Thread(target=tarea2)

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Esperar a que los hilos terminen
hilo1.join()
hilo2.join()

print("Ejecución finalizada")