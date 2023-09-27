import datetime
from collections import deque


class Vuelo:
    def __init__(self, numero_vuelo, tipo_vuelo, hora_programada, duracion, prioridad, estado):
        self.numero_vuelo = numero_vuelo
        self.tipo_vuelo = tipo_vuelo
        self.hora_programada = hora_programada
        self.duracion = duracion
        self.prioridad = prioridad
        self.estado = estado

class ControlTraficoAereo:
    def __init__(self):
        self.cola_aterrizar = deque()
        self.cola_despegar = deque()
        self.vuelos_aterrizados = []
        self.vuelos_despegados = []
        self.tiempo_rotacion = datetime.timedelta(minutes=3)

    def agregar_vuelo(self, vuelo):
        if vuelo.tipo_vuelo == "Llegada":
            self.cola_aterrizar.append(vuelo)
        elif vuelo.tipo_vuelo == "Salida":
            self.cola_despegar.append(vuelo)

    def eliminar_vuelo(self, vuelo):
        if vuelo.tipo_vuelo == "Llegada":
            self.cola_aterrizar.remove(vuelo)
            self.vuelos_aterrizados.append(vuelo)
        elif vuelo.tipo_vuelo == "Salida":
            self.cola_despegar.remove(vuelo)
            self.vuelos_despegados.append(vuelo)

    def manejar_prioridad(self):
        self.cola_aterrizar = deque(sorted(self.cola_aterrizar, key=lambda x: (x.prioridad, x.estado)))
        self.cola_despegar = deque(sorted(self.cola_despegar, key=lambda x: (x.prioridad, x.estado)))

    def mostrar_informacion_vuelos(self):
        print("Información de Vuelos en Espera:")
        print("\nVuelos en Espera para Aterrizar:")
        for vuelo in self.cola_aterrizar:
            tiempo_espera = (datetime.datetime.now() - vuelo.hora_programada).total_seconds() / 60
            print(f"Número de Vuelo: {vuelo.numero_vuelo}")
            print(f"Hora Programada: {vuelo.hora_programada.strftime('%H:%M:%S')}")
            print(f"Duración (min): {vuelo.duracion}")
            print(f"Prioridad: {vuelo.prioridad}")
            print(f"Estado: {vuelo.estado}")
            print(f"Tiempo de Espera (min): {tiempo_espera:.2f}")
            print()
        print("\nVuelos en Espera para Despegar:")
        for vuelo in self.cola_despegar:
            tiempo_espera = (datetime.datetime.now() - vuelo.hora_programada).total_seconds() / 60
            print(f"Número de Vuelo: {vuelo.numero_vuelo}")
            print(f"Hora Programada: {vuelo.hora_programada.strftime('%H:%M:%S')}")
            print(f"Duración (min): {vuelo.duracion}")
            print(f"Prioridad: {vuelo.prioridad}")
            print(f"Estado: {vuelo.estado}")
            print(f"Tiempo de Espera (min): {tiempo_espera:.2f}")
            print()

    def validar_numero_vuelo(self, numero_vuelo):
        if len(numero_vuelo) == 6 and numero_vuelo.isalnum():
            return True
        return False

    def solicitud_despegar(self):
        numero_vuelo = input("Ingrese el número de vuelo para despegar (6 caracteres alfanuméricos): ")
        tipo_vuelo = "Salida"
        hora_programada = datetime.datetime.now() + datetime.timedelta(minutes=len(self.cola_despegar) * 3)
        duracion = int(input("Ingrese la duración del vuelo (en minutos): "))
        prioridad = input("Ingrese la prioridad (Comercial, Militar, Especial, Emergencia): ")
        estado = input("Ingrese el estado (On time, Delayed, Cancelled): ")

        if self.validar_numero_vuelo(numero_vuelo):
            vuelo = Vuelo(numero_vuelo, tipo_vuelo, hora_programada, duracion, prioridad, estado)
            self.agregar_vuelo(vuelo)
            print("Vuelo agregado a la cola de despegue.")
        else:
            print("Número de vuelo no válido. Debe tener 6 caracteres alfanuméricos.")

    def solicitud_aterrizar(self):
        numero_vuelo = input("Ingrese el número de vuelo para aterrizar (6 caracteres alfanuméricos): ")
        tipo_vuelo = "Llegada"
        hora_programada = datetime.datetime.now() + datetime.timedelta(minutes=len(self.cola_aterrizar) * 3)
        duracion = int(input("Ingrese la duración del vuelo (en minutos): "))
        prioridad = input("Ingrese la prioridad (Comercial, Militar, Especial, Emergencia): ")
        estado = input("Ingrese el estado (On time, Delayed, Cancelled): ")

        if self.validar_numero_vuelo(numero_vuelo):
            vuelo = Vuelo(numero_vuelo, tipo_vuelo, hora_programada, duracion, prioridad, estado)
            self.agregar_vuelo(vuelo)
            print("Vuelo agregado a la cola de aterrizaje.")
        else:
            print("Número de vuelo no válido. Debe tener 6 caracteres alfanuméricos.")

    def ejecutar(self):
        while True:
            print("\nOpciones:")
            print("1. Despegar")
            print("2. Aterrizar")
            print("3. Mostrar Información de Vuelos")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.solicitud_despegar()
            elif opcion == "2":
                self.solicitud_aterrizar()
            elif opcion == "3":
                self.manejar_prioridad()
                self.mostrar_informacion_vuelos()
            elif opcion == "4":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    control = ControlTraficoAereo()
    control.ejecutar()