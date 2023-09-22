class Flight:
    def __init__(self):
        self.rows = 27
        self.seats_per_row = 6
        self.seats = {}
        self.passenger_info = {}

        for row in range(1, self.rows + 1):
            for seat_letter in ["A", "B", "C", "H", "J", "K"]:
                seat_number = f"{row}{seat_letter}"
                self.seats[seat_number] = "libre"

    def get_seat_status(self, seat_number):
        return self.seats.get(seat_number, "invalid")

    def reserve_seat(self, seat_number, passenger_name, id_number):
        if self.get_seat_status(seat_number) == "libre":
            self.seats[seat_number] = "reservada"
            self.passenger_info[seat_number] = {"name": passenger_name, "id": id_number}
            return True
        return False

    def assign_ticket(self, seat_number):
        if self.get_seat_status(seat_number) == "reservada":
            ticket_number = f"TKT-{seat_number}"
            self.seats[seat_number] = ticket_number
            return ticket_number
        return None

    def is_valid_row(self, row):
        return 5 <= row <= 27

    def print_seat_status(self):
        print("\nECONOMY\nCLASS: ", "A".center(7), "B".center(6), "C".center(6), "H".center(6), "J".center(6), "K".center(6))
        for row in range(5, 28):
            row_status = []
            for seat_letter in ["A", "B", "C", "H", "J", "K"]:
                seat_number = f"{row}{seat_letter}"
                row_status.append(self.seats[seat_number])
            print(f"Fila {row:2}: {', '.join(row_status)}")

# Crear una instancia de Flight
flight = Flight()

def menu():
    while True:
        print("\nMenú:")
        print("1. Reservar puesto")
        print("2. Ver disponibilidad")
        print("3. Consultar reserva")
        print("4. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            seat_number = input("Ingrese el número de puesto a reservar (por ejemplo, 5B): ")
            row = int(seat_number[:-1])
            if flight.is_valid_row(row):
                passenger_name = input("Ingrese su nombre completo: ")
                id_number = input("Ingrese su número de identificación: ")
                if flight.reserve_seat(seat_number, passenger_name, id_number):
                    print("Puesto reservado exitosamente.")
                    ticket_number = flight.assign_ticket(seat_number)
                    print(f"Su número de ticket es: {ticket_number}")
                else:
                    print("El puesto no está disponible para reservar.")
            else:
                print("Error: El número de fila no es válido.")

        elif choice == "2":
            flight.print_seat_status()

        elif choice == "3":
            ticket_number = input("Ingrese su número de ticket: ")
            seat_number = ticket_number.split("-")[1]
            status = flight.get_seat_status(seat_number)
            if status == ticket_number:
                passenger_info = flight.passenger_info.get(seat_number, {})
                if passenger_info:
                    print(f"Estado de la reserva para el ticket {ticket_number}: {status}")
                    print(f"Nombre del pasajero: {passenger_info['name']}")
                    print(f"Número de identificación: {passenger_info['id']}")
                else:
                    print("Información de pasajero no encontrada.")
            else:
                print("Ticket no encontrado.")

        elif choice == "4":
            flight.print_seat_status()
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()

