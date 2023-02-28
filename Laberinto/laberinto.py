# import random

# matriz = []

# for i in range(10):
#     fila = []
#     for j in range(10):
#         elemento = random.choice([-1, 0, 1])
#         fila.append(elemento)
#     matriz.append(fila)

# # Imprimimos la matriz generada
# for fila in matriz:
#     print(fila)


# 2 version funcional pero en diagonal
import random
from collections import deque

# Definimos la posición de inicio y de la meta
inicio = (0, 0)
meta = (9, 9)

# Definimos una función que verifica si una posición es válida


def es_valida(x, y, laberinto):
    if x < 0 or x >= len(laberinto) or y < 0 or y >= len(laberinto[0]):
        return False
    if laberinto[x][y] == 1:
        return False
    return True

# Definimos la función BFS que busca una solución en el laberinto


def bfs(laberinto, inicio, meta):
    visitados = set()
    cola = deque()
    cola.append((inicio, []))
    while cola:
        nodo, camino = cola.popleft()
        if nodo == meta:
            return camino + [nodo]
        if nodo in visitados:
            continue
        visitados.add(nodo)
        x, y = nodo
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if es_valida(nx, ny, laberinto):
                cola.append(((nx, ny), camino + [nodo]))
    return None


# Generamos la matriz del laberinto

matriz = []

for i in range(10):
    fila = []
    for j in range(10):
        elemento = random.choice([-1, 0, 1])
        fila.append(elemento)
    matriz.append(fila)

# Imprimimos la matriz generada
for fila in matriz:
    print(fila)

# Buscamos una solución desde el inicio hasta la meta
solucion = bfs(matriz, inicio, meta)
# Imprimimos la solución encontrada, resaltando el camino en "X"
if solucion:
    print("Se encontró una solución:")
    for fila in matriz:
        print(fila)
    for i, j in solucion:
        fila = ["." if (i, y) != (
            i, j) else "X" for y in range(len(matriz[0]))]
        print(" ".join(str(x) for x in fila))
else:
    print("No se encontró una solución.")

# 3 Genera pero con diagonal
# import random
# from collections import deque

# # Definimos la posición de inicio y de la meta
# inicio = (0, 0)
# meta = (9, 9)

# # Definimos una función que verifica si una posición es válida


# def es_valida(x, y, laberinto):
#     if x < 0 or x >= len(laberinto) or y < 0 or y >= len(laberinto[0]):
#         return False
#     if laberinto[x][y] == 1:
#         return False
#     return True

# # Definimos la función BFS que busca una solución en el laberinto


# def bfs(laberinto, inicio, meta):
#     visitados = set()
#     cola = deque()
#     cola.append((inicio, []))
#     while cola:
#         nodo, camino = cola.popleft()
#         if nodo == meta:
#             return camino + [nodo]
#         if nodo in visitados:
#             continue
#         visitados.add(nodo)
#         x, y = nodo
#         for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             nx, ny = x + dx, y + dy
#             if es_valida(nx, ny, laberinto):
#                 cola.append(((nx, ny), camino + [nodo]))
#     return None


# # Generamos la matriz del laberinto
# matriz = []
# for i in range(10):
#     fila = []
#     for j in range(10):
#         elemento = random.choice([-1, 0, 1])
#         fila.append(elemento)
#     matriz.append(fila)

# # Imprimimos la matriz generada
# for fila in matriz:
#     print(fila)

# # Buscamos una solución desde el inicio hasta la meta
# solucion = bfs(matriz, inicio, meta)

# # Imprimimos la solución encontrada, resaltando el camino en "X"
# if solucion:
#     print("Se encontró una solución:")
#     for fila in matriz:
#         print(fila)
#     for i, j in solucion:
#         fila = ["." if (i, y) != (
#             i, j) else "X" for y in range(len(matriz[0]))]
#         print(" ".join(str(x) for x in fila))
# else:
#     print("No se encontró una solución.")

# 4
# import random
# from collections import deque

# # Definimos la posición de inicio y de la meta
# inicio = (0, 0)
# meta = (9, 9)

# # Definimos una función que verifica si una posición es válida


# def es_valida(x, y, laberinto):
#     if x < 0 or x >= len(laberinto) or y < 0 or y >= len(laberinto[0]):
#         return False
#     if laberinto[x][y] == 1:
#         return False
#     return True

# # Definimos la función BFS que busca una solución en el laberinto


# def bfs(laberinto, inicio, meta):
#     visitados = set()
#     cola = deque()
#     cola.append((inicio, []))
#     while cola:
#         nodo, camino = cola.popleft()
#         if nodo == meta:
#             return camino + [nodo]
#         if nodo in visitados:
#             continue
#         visitados.add(nodo)
#         x, y = nodo
#         for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             if dx != 0 and dy != 0:
#                 continue
#             nx, ny = x + dx, y + dy
#             if es_valida(nx, ny, laberinto):
#                 cola.append(((nx, ny), camino + [nodo]))
#     return None


# # Generamos la matriz del laberinto
# matriz = []
# for i in range(10):
#     fila = []
#     for j in range(10):
#         elemento = random.choice([-1, 0, 1])
#         fila.append(elemento)
#     matriz.append(fila)

# # Imprimimos la matriz generada
# for fila in matriz:
#     print(fila)

# # Buscamos una solución desde el inicio hasta la meta
# solucion = bfs(matriz, inicio, meta)

# # Imprimimos la solución encontrada, resaltando el camino en "X"
# if solucion:
#     print("Se encontró una solución:")
#     for fila in matriz:
#         print(fila)
#     for i, j in solucion:
#         fila = ["." if (i, y) != (
#             i, j) else "X" for y in range(len(matriz[0]))]
#         print(" ".join(str(x) for x in fila))
# else:
#     print("No se encontró una solución.")


# 5
# import random
# from collections import deque

# # Definimos la posición de inicio y de la meta
# inicio = (0, 0)
# meta = (9, 9)

# # Definimos una función que verifica si una posición es válida


# def es_valida(x, y, laberinto):
#     if x < 0 or x >= len(laberinto) or y < 0 or y >= len(laberinto[0]):
#         return False
#     if laberinto[x][y] != 0:
#         return False
#     return True

# # Definimos la función BFS que busca una solución en el laberinto


# def bfs(laberinto, inicio, meta):
#     visitados = set()
#     cola = deque()
#     cola.append((inicio, []))
#     while cola:
#         nodo, camino = cola.popleft()
#         if nodo == meta:
#             return camino + [nodo]
#         if nodo in visitados:
#             continue
#         visitados.add(nodo)
#         x, y = nodo
#         for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             if dx != 0 and dy != 0:
#                 continue
#             nx, ny = x + dx, y + dy
#             if es_valida(nx, ny, laberinto):
#                 cola.append(((nx, ny), camino + [nodo]))
#     return None


# # Generamos la matriz del laberinto
# matriz = []
# for i in range(10):
#     fila = []
#     for j in range(10):
#         if i == 0 and j == 0:  # Posición de inicio
#             fila.append(0)
#         elif i == 9 and j == 9:  # Posición de meta
#             fila.append(0)
#         else:
#             # Agregamos un elemento aleatorio entre 0 y 1 (inclusive)
#             # para permitir que el laberinto tenga más de una solución
#             fila.append(random.randint(0, 1))
#     matriz.append(fila)

# # Imprimimos la matriz generada
# for fila in matriz:
#     print(fila)

# # Buscamos una solución desde el inicio hasta la meta
# solucion = bfs(matriz, inicio, meta)

# # Imprimimos la solución encontrada, resaltando el camino en "X"
# if solucion:
#     print("Se encontró una solución:")
#     for fila in matriz:
#         print(fila)
#     for i, j in solucion:
#         fila = ["." if (i, y) != (
#             i, j) else "X" for y in range(len(matriz[0]))]
#         print(" ".join(str(x) for x in fila))
# else:
#     print("No se encontró una solución.")
