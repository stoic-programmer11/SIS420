class Tablero:
    def __init__(self):
        self.estado = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def get_posiciones_vacias(self):
        posiciones_vacias = []
        for i in range(3):
            for j in range(3):
                if self.estado[i][j] == ' ':
                    posiciones_vacias.append((i, j))
        return posiciones_vacias

    def marcar_posicion(self, fila, columna, letra):
        self.estado[fila][columna] = letra

    def imprimir_tablero(self):
        for i in range(3):
            print('-------------')
            for j in range(3):
                print(f'| {self.estado[i][j]} ', end='')
            print('|')
        print('-------------')

    def contar_uniones(self):
        uniones = {'X': 0, 'O': 0}

        for i in range(3):
            for j in range(2):
                if self.estado[i][j] == self.estado[i][j + 1] and self.estado[i][j] != ' ':
                    uniones[self.estado[i][j]] += 1
                if self.estado[j][i] == self.estado[j + 1][i] and self.estado[j][i] != ' ':
                    uniones[self.estado[j][i]] += 1

        return uniones


def minimax(tablero, es_maximizador, alfa, beta):
    uniones = tablero.contar_uniones()
    if uniones['X'] >= 3 or uniones['O'] >= 3:
        if es_maximizador:
            return (-1, None)
        else:
            return (1, None)
    posiciones_vacias = tablero.get_posiciones_vacias()
    if not posiciones_vacias:
        return (0, (None, None))  # Devuelve en lugar de None
    if es_maximizador:
        mejor_puntuacion = float('-inf')
        mejor_posicion = None
        for fila, columna in posiciones_vacias:
            tablero.marcar_posicion(fila, columna, 'O')
            puntuacion = minimax(tablero, False, alfa, beta)[0]
            tablero.marcar_posicion(fila, columna, ' ')
            if puntuacion > mejor_puntuacion:
                mejor_puntuacion = puntuacion
                mejor_posicion = (fila, columna)
            alfa = max(alfa, mejor_puntuacion)
            if beta <= alfa:
                break
        return (mejor_puntuacion, mejor_posicion)
    else:
        mejor_puntuacion = float('inf')
        mejor_posicion = None
        for fila, columna in posiciones_vacias:
            tablero.marcar_posicion(fila, columna, 'X')
            puntuacion = minimax(tablero, True, alfa, beta)[0]
            tablero.marcar_posicion(fila, columna, ' ')
            if puntuacion < mejor_puntuacion:
                mejor_puntuacion = puntuacion
                mejor_posicion = (fila, columna)
            beta = min(beta, mejor_puntuacion)
            if beta <= alfa:
                break
        return (mejor_puntuacion, mejor_posicion)


if __name__ == "__main__":

    tablero = Tablero()

    letra_jugador = input("Elige una letra entre 'O' y 'X': ")
    while letra_jugador not in ['O', 'X']:
        letra_jugador = input("Elige una letra entre 'O' y 'X': ")

    letra_ordenador = 'O' if letra_jugador == 'X' else 'X'

    # Determinar quién comienza
    jugador_comienza = input("Quieres Jugar Primero? (S/N): ")
    if jugador_comienza.lower() == 's':
        es_turno_jugador = True
    else:
        es_turno_jugador = False

    # Loop principal del juego
while True:
    if es_turno_jugador:
        # Pedir al jugador que elija una posición para marcar
        print("Es tu turno")
        fila = int(input("Elige la fila (1-3): ")) - 1
        columna = int(input("Elige la columna (1-3): ")) - 1
        while tablero.estado[fila][columna] != ' ':
            print("Esa posición ya está ocupada. Elige otra.")
            fila = int(input("Elige la fila (1-3): ")) - 1
            columna = int(input("Elige la columna (1-3): ")) - 1
        tablero.marcar_posicion(fila, columna, letra_jugador)
        es_turno_jugador = False
    else:
        uniones = tablero.contar_uniones()
        if uniones['X'] >= 3 or uniones['O'] >= 3 or not tablero.get_posiciones_vacias():
            break
        # Calcular la mejor posición para que marque el ordenador
        print("Es el turno de la computadora")
        _, (fila, columna) = minimax(
            tablero, True, float('-inf'), float('inf'))
        tablero.marcar_posicion(fila, columna, letra_ordenador)
        es_turno_jugador = True

    # Imprimir el estado actual del tablero
    tablero.imprimir_tablero()

# Verificar si hay ganador o empate
uniones = tablero.contar_uniones()
if uniones['X'] >= 3 or uniones['O'] >= 3:
    if uniones[letra_jugador] > uniones[letra_ordenador]:
        print(
            f"Ganaste! Uniones {letra_jugador}: {uniones[letra_jugador]}, Uniones {letra_ordenador}: {uniones[letra_ordenador]}")
    elif uniones[letra_jugador] < uniones[letra_ordenador]:
        print(
            f"Perdiste! Uniones {letra_jugador}: {uniones[letra_jugador]}, Uniones {letra_ordenador}: {uniones[letra_ordenador]}")
    else:
        print("Empate!")
else:
    print("Empate!")
