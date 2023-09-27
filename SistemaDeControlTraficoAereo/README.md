Control de Tráfico Aéreo
=
¡Bienvenido al Desafío de Implementación del Sistema de Control de Tráfico Aéreo! Imagina que trabajas en una compañía de aviación y tienes la tarea de crear un sistema que gestione el despegue y aterrizaje de aviones en un aeropuerto. Este sistema es crucial para garantizar un flujo seguro y eficiente de vuelos.

![image](https://github.com/MinhyukHong/Estructura-de-Datos/assets/108979014/fd670576-1406-4188-bb15-af7d6e044e03)


## Descripción del Desafío
El objetivo de este proyecto es implementar un sistema de control de tráfico aéreo capaz de gestionar la llegada y salida de vuelos en un aeropuerto. El sistema debe tener en cuenta varios factores, como la disponibilidad y duración de las pistas, la hora programada de llegada o salida de cada avión, la prioridad de cada vuelo y el estado del vuelo (puntual, retrasado o cancelado).

## Requerimientos
1. Añadir Vuelos: El sistema debe permitir agregar nuevos vuelos a la cola de espera para aterrizar o despegar. Cada vuelo debe tener la siguiente información:
* Número de vuelo.
* Tipo de vuelo (llegada o salida).
* Hora programada de llegada o salida.
* Duración del vuelo.
* Prioridad (comercial, militar, especial o en emergencia).
* Estado (On time, Delayed o Cancelled).
2. Eliminar Vuelos: El sistema debe permitir eliminar un vuelo de la cola una vez que aterrice o despegue.
3. Gestión de Prioridad: El sistema debe ser capaz de manejar la prioridad de los vuelos, ya sea por prioridad o por estado.
4. Visualización de Información: El sistema debe mostrar la siguiente información:
* Cantidad de vuelos en espera para aterrizar.
* Cantidad de vuelos que han aterrizado.
* Cantidad de vuelos que han despegado.
* Información detallada de cada vuelo en espera, incluyendo número de vuelo, hora programada, duración, prioridad y tiempo de espera.
5. Eficiencia y Escalabilidad: El diseño de la estructura de datos y las operaciones con los datos debe ser eficiente y escalable.
6. Intervalo de Despegue/Aterrizaje: Los aviones despegan o aterrizan cada 3 minutos por los puntos de rotación del aire, tenlo en cuenta en tu implementación.

## Consejos
1. Puedes utilizar una estructura de datos en cola (o fila) para representar cada vuelo y su información, como número de vuelo, tipo de vuelo, hora programada, duración, prioridad y estado.
2. Para mostrar la información de los vuelos en espera, considera agregar una interfaz de usuario sencilla que muestre los detalles de cada vuelo, incluyendo el tiempo de espera. Puedes utilizar texto por consola o, si trabajas en Python, puedes explorar la opción de utilizar PySimpleGUI para crear una interfaz gráfica opcional.
3. Asegúrate de que tu sistema sea eficiente y escalable al seleccionar las estructuras de datos adecuadas para gestionar las colas y las filas.
