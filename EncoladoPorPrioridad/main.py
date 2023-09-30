import heapq
from collections import defaultdict


class EncoladoPorPrioridad:

    def __init__(self):
        self.queue = []

    def push(self, item):
        heapq.heappush(self.queue, item)

    def pop(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0


elementos_mismo_prioridad = defaultdict(list)

while True:
    nombre = input("Ingrese el nombre (El programa terminará si ingresa 'fin'): ")
    if nombre == 'fin':
        break
    prioridad = input("Ingrese la prioridad (A, B o C): ")

    orden_prioridad = 0 if prioridad == 'A' else 1 if prioridad == 'B' else 2
    elementos_mismo_prioridad[orden_prioridad].append((nombre, prioridad))

    print("\nElementos de Queue de acuerdo con la Prioridad:")
    print("Nombre\tPrioridad")

    for priority in range(3):
        elementos_mismo_prioridad[priority].sort(key=lambda x: x[1])
        for nombre, display_prioridad in elementos_mismo_prioridad[priority]:
            print(f"{nombre}\t{display_prioridad}")