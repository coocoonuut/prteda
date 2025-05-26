import networkx as conexion

# vertices = ["A", "B", "C", "D"]

n = int(input("¿Cuantos vertices tendra el grafo? "))

print("\nIngresa el nombre de cada vertice")

vertices = []
for i in range(n):
    vertice = input(f"Nombre del vertice {i + 1}: ")
    vertices.append(vertice)

# Matriz de Adyacencia con pesos (0 = sin conexion)
# aristas = [[0, 10, 15, 0], [10, 0, 4, 25], [15, 4, 0, 30], [0, 25, 30, 0]]
print("\nIngresa la Matriz de Adyacencia (separada por espacios por fila)")

aristas = []
for i in range(n):
    fila = list(map(int, input(f"Fila {i + 1}: ").split()))
    aristas.append(fila)

grafo_dirigido = conexion.DiGraph()
grafo_dirigido.add_nodes_from(vertices)

# Agregar aristas con pesos desde la matriz
for i in range(len(vertices)):
    for j in range(len(vertices)):
        peso = aristas[i][j]
        if peso != 0:
            grafo_dirigido.add_edge(vertices[i], vertices[j], weight=peso)

origen = input("\nVertice origen: ")
destino = input("Vertice destino: ")

ruta_corta = conexion.dijkstra_path(grafo_dirigido, source=origen, target=destino)
costo_total = conexion.dijkstra_path_length(
    grafo_dirigido, source=origen, target=destino
)

print(f"\nRuta más corta desde {origen} hasta {destino}:")

for i in range(len(ruta_corta) - 1):
    a, b = ruta_corta[i], ruta_corta[i + 1]
    peso = grafo_dirigido[a][b]["weight"]
    print(f"{a} -> {b} = {peso}")

print(f"\nDistancia total: {costo_total}")
