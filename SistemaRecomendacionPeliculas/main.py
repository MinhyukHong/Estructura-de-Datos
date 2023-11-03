import matplotlib.pyplot as plt
import networkx as nx


class SistemaRecomendacionPeliculas:
    def __init__(self, datos_peliculas):
        self.G = nx.Graph()
        self.datos_peliculas = datos_peliculas
        self.construir_grafo()
    
    def construir_grafo(self):
        for i in range(len(self.datos_peliculas)):
            pelicula1 = self.datos_peliculas[i]
            for j in range(i + 1, len(self.datos_peliculas)):
                pelicula2 = self.datos_peliculas[j]
                generos1 = set(pelicula1[4].split(","))
                generos2 = set(pelicula2[4].split(","))
                similitud = len(generos1.intersection(generos2))
                if similitud > 0:
                    self.G.add_edge(pelicula1[0], pelicula2[0], peso=similitud)

    def recomendar_pelicula(self, titulo_pelicula):
        if titulo_pelicula not in self.G:
            return "No se encontró la película."
        
        recomendaciones = []
        for pelicula, w in self.G[titulo_pelicula].items():
            recomendaciones.append((pelicula, w["peso"]))
        
        recomendaciones.sort(key=lambda x: x[1], reverse=True)
        return recomendaciones

    def pelicula_mejor_valorada(self):
        mejor_puntuacion = -1
        mejor_pelicula = None

        for pelicula in self.datos_peliculas:
            titulo, year, director, productora, genero, puntuacion = pelicula
            if puntuacion > mejor_puntuacion:
                mejor_pelicula = titulo
                mejor_puntuacion = puntuacion

        return mejor_pelicula, mejor_puntuacion

    
# Ejemplo de uso
datos_peliculas = [
    ["El sabor de la victoria", 2006, "Madison Alexander", "Paramount Pictures", "Aventura", 2.6],
    ["La hora del juicio", 1990, "William Emma", "Sony Pictures", "Fantasía", 6],
    ["La promesa de la justicia", 2001, "Matthew Lucy", "Paramount Pictures", "Animación", 6],
    ["El legado de la venganza", 1984, "David Robert", "20th Century Fox", "Comedia", 3.1],
    ["El legado del héroe", 2004, "Benjamin Noah", "Walt Disney Pictures", "Ciencia Ficción", 0.1],
    ["La leyenda de la justicia", 2002, "Alexander James", "Sony Pictures", "Comedia", 7.1],
    ["El fuego de la venganza", 1993, "Noah Abigail", "Warner Bros.", "Animación", 6.7],
    ["La última oportunidad", 2022, "Abigail Isabella", "Walt Disney Pictures", "Horror", 5],
    ["El fuego de la venganza", 2002, "Michael Isabella", "Warner Bros.", "Documental", 8],
    ["El camino de la venganza", 1987, "Elijah Emma", "Paramount Pictures", "Documental", 8.1]
]

sistema_peliculas = SistemaRecomendacionPeliculas(datos_peliculas)
pelicula_a_recomendar = "El fuego de la venganza"
recomendaciones = sistema_peliculas.recomendar_pelicula(pelicula_a_recomendar)
mejor_pelicula, puntuacion = sistema_peliculas.pelicula_mejor_valorada()

# Visualización del grafo
pos = nx.kamada_kawai_layout(sistema_peliculas.G)
plt.figure(figsize=(10, 5))
nx.draw(sistema_peliculas.G, pos, with_labels=True, node_size=300, node_color='skyblue', font_size=10, font_color='black')
plt.title("Grafo de Películas basado en similitud de géneros")
plt.show()

print(f"Si te gusta '{pelicula_a_recomendar}', las películas recomendadas son:")
if isinstance(recomendaciones, str):
    print(recomendaciones)
else:
    for pelicula, peso in recomendaciones:
        print(f"{pelicula} (Similitud: {peso})")

print(f"\nLa película mejor valorada es:\n'{mejor_pelicula}' con una puntuación de {puntuacion}")