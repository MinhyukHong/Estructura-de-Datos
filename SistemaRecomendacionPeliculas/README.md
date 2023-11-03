Sistema de<br>
Recomendación de<br>
Películas
=
Este proyecto implementa un sistema de recomendación de películas utilizando Python. El sistema se basa en la similitud de géneros entre películas para recomendar películas relacionadas. Aquí se presenta la visualización del grafo de películas y un ejemplo de ejecución.

## Visualización del Grafo
El grafo de películas se visualiza utilizando el algoritmo "Kamada-Kawai" proporcionado por NetworkX. Este algoritmo se encarga de distribuir los nodos en el grafo de manera que las aristas más cortas sean más visibles. A continuación, se muestra cómo se ve el grafo de películas:

![image](https://github.com/MinhyukHong/Estructura-de-Datos/assets/108979014/8e0d5005-4113-4b16-bebd-3dcd0f7cb938)


# Algoritmo de Visualización del Grafo
Puedes cambiar el algoritmo de visualización del grafo reemplazando nx.kamada_kawai_layout con otros algoritmos de NetworkX, como nx.spring_layout o nx.circular_layout. Aquí hay un ejemplo de cómo cambiar el algoritmo de visualización:<br>


Utiliza el algoritmo de disposición "Spring" para la visualización del grafo.<br>
```bash
pos = nx.spring_layout(sistema_peliculas.G)
```

## Tipos de Layout 
1. spring_layout(G)

![image](https://github.com/MinhyukHong/Estructura-de-Datos/assets/108979014/482b0603-d63c-46ec-81fb-07654cdbd0ec)


2. kamada_kawai_layout(G)

![image](https://github.com/MinhyukHong/Estructura-de-Datos/assets/108979014/705da6d4-02e3-4229-8d83-bd60edbd63ea)


3. shell_layout(G) , circular_layout(G)

![image](https://github.com/MinhyukHong/Estructura-de-Datos/assets/108979014/e065af26-8e0a-4781-95c0-d5bc65d3150b)


4. random_layout(G)

![image](https://github.com/MinhyukHong/Estructura-de-Datos/assets/108979014/fbccd80b-20f3-4082-a6d7-e37ae3b04659)


5. spectral_layout(G)

![image](https://github.com/MinhyukHong/Estructura-de-Datos/assets/108979014/9a27dfcc-fd3d-454f-aff4-86b8c4524ad0)


6. fruchterman_reingold_layout(G)

![image](https://github.com/MinhyukHong/Estructura-de-Datos/assets/108979014/460b487d-22d3-470b-bbc2-852d00deceb9)


