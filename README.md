# HILOS

## ¿Cómo se crean los Hilos?
Los hilos se crean utilizando la clase Thread del módulo threading. A cada hilo se le asigna una función mediante el parámetro target, que define la tarea que ejecutará.

## ¿Qué tarea ejecuta cada hilo?
- Hilo 1: ejecuta la función tarea1, que imprime números del 0 al 4 con una pausa de un segundo.
- Hilo 2: ejecuta la función tarea2, realizando la misma operación de forma independiente.

## ¿Qué sucede durante la ejecución concurrente?
Ambos hilos se ejecutan al mismo tiempo, lo que provoca que los mensajes en consola aparezcan intercalados. Esto demuestra la concurrencia, ya que el programa no espera a que un hilo termine para iniciar el otro.