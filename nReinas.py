# ----------------------------------------------------------------
# Funciones para manejar la pila
# ----------------------------------------------------------------


def push(lista, e):
    return lista.append(e)


def top(lista):
    return lista[-1]


def pop(lista):
    return lista.pop(-1)


def isEmpty(lista):
    return len(lista) == 0


def size(lista):
    return len(lista)


# ----------------------------------------------------------------
# Funciones para manejar una matriz
# ----------------------------------------------------------------


def fila_nula(n):
    return [0]*n


def matriz_nula(n):
    return [[0]*n for i in range(n)]


def printMatriz(matriz):
    unix_rojo = "\033[0;31m"
    unix_limpiar_color = "\033[0m"
    print()
    for i in range(len(matriz)):
        print("|", end="")
        for j in range(len(matriz[0])):
            if matriz[i][j] == 1:
                print(unix_rojo + "R" + unix_limpiar_color, end="|")
            else:
                print("*", end="|")
        print()
    print()


def copiarMatriz(matriz):
    n = len(matriz)
    matrizNueva = matriz_nula(n)
    for i in range(n):
        for j in range(n):
            matrizNueva[i][j] = matriz[i][j]
    return matrizNueva

# ----------------------------------------------------------------
# Funciones para manejar el backtracking
# ----------------------------------------------------------------


def es_solucion(matriz):
    n = len(matriz)
    reinas = 0
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                reinas += 1
    return reinas == n


def es_valida(matriz, fila, col):
    n = len(matriz)
    # Revisa la columna
    for i in range(fila):
        if matriz[i][col] == 1:
            return False

    # Revisa la diagonal /
    j = col + 1
    for i in range(fila - 1, -1, -1):
        if j < n:
            if matriz[i][j] == 1:
                return False
            j += 1

    # Revisa la diagonal \
    j = col - 1
    for i in range(fila - 1, -1, -1):
        if j >= 0:
            if matriz[i][j] == 1:
                return False
            j -= 1

    return True


def obtener_hijos(matriz):
    # Busca la prox fila sin reinas
    n = len(matriz)
    fila = -1
    for i in range(n):
        if 1 not in matriz[i]:
            fila = i
            break

    if fila == -1:
        return []  # No tiene hijos (es una posible solucion)

    hijos = []
    for col in range(n-1, -1, -1): # Recorre las columnas de derecha a izquierda ya que la pilas es FILO
        if es_valida(matriz, fila, col):
            nMatriz = copiarMatriz(matriz)
            nMatriz[fila][col] = 1
            hijos.append(nMatriz)
    return hijos

# ----------------------------------------------------------------
# DFS para recorrer el grafo con las combinaciones
# ----------------------------------------------------------------


def n_reinas(raiz):
    '''
    Obtine solo la primera solucion
    '''
    # soluciones = []
    pila = []
    push(pila, raiz)

    while (not isEmpty(pila)):
        estado = pop(pila)
        if (es_solucion(estado)):
            # soluciones.append(estado)
            return estado
        hijos = obtener_hijos(estado)
        for hijo in hijos:
            push(pila, hijo)

    return []  # soluciones


def main():
    n = int(input("Ingrese un n: "))

    print("Primera solucion:")
    raiz = matriz_nula(n)
    printMatriz(n_reinas(raiz))


if __name__ == '__main__':
    main()
