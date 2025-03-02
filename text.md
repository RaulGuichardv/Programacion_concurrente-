# PROGRAMACIÓN CONCURRENTE, SECUENCIAL, PARALELA

## SECUENCIAL
- Ejecuta una tarea de una aplicación de manera lineal y una por una. Esto quiere decir que hasta que no finaliza con una tarea, no avanza a la siguiente.

## CONCURRENTE
- Permite que una aplicación pueda realizar varias tareas al mismo tiempo. Para ello, se pueden generar varios hilos de ejecución o repartir las ejecuciones entre varios núcleos de la CPU, consiguiendo ejecuciones simultáneas y paralelas de distintos hilos de ejecución.

## CONCURRENCIA EN PYTHON
- En el caso de Python, y debido al GIL (Global Interpreter Lock), la programación concurrente solamente es posible mediante la creación de hilos que se ejecuten en distintos núcleos del CPU. Si no implementamos esta metodología, aunque podamos crear varios hilos, seguimos teniendo un único flujo de ejecución. Sin embargo, la mayoría de las veces podemos simular el comportamiento de la programación concurrente, ya que dicho flujo se intercambia entre los distintos hilos muy rápidamente, dando la sensación de que estamos realizando varias tareas al mismo tiempo, a pesar de que las instrucciones del código siguen ejecutándose de manera secuencial.

Por lo tanto, para implementar la programación concurrente en Python tenemos básicamente dos opciones:

- **Crear varios hilos que son capaces de comunicarse entre sí** (comparten memoria). El orden de ejecución de sus tareas sigue siendo secuencial.
- **Crear varios hilos que no son capaces de comunicarse entre sí** (no comparten memoria). Se ejecutan en distintos núcleos del CPU.

## Librerías para Programación Concurrente en Python

En Python disponemos de tres librerías principales para crear programas que implementen o simulen la programación concurrente:

### **Threading** (Simula Programación Concurrente)
- El orden de ejecución de las distintas partes de cada hilo se realiza de manera "aleatoria", en función de las decisiones que tome el propio sistema.

### **Asyncio** (Simula Programación Concurrente)
- Funciona de manera similar a **Threading**, pero en este caso tendremos más control sobre el orden de ejecución de las distintas partes de cada hilo.

### **Multiprocessing** (Implementa Programación Concurrente)
- Reparte los distintos hilos creados entre varios de los núcleos del CPU del sistema donde se va a ejecutar la aplicación, lo que permite ejecutar las tareas de manera paralela. En este caso, en Python es la única librería que ofrece programación concurrente real, aunque consume más recursos.  
- A diferencia de las anteriores, **no se comparte la memoria** entre los distintos hilos de ejecución.
