# Pregunta 1
def menor(a, b):
    return a < b


def relacion(A, B, P):
    resultado = []
    for a in A:
        for b in B:
            if P(a, b):
                resultado.append((a, b))
    return resultado


print(relacion([1, 3], [3, 5], menor))


# Pregunta 2
def transpuesta(matriz):
    n, m = len(matriz), len(matriz[0])
    res = []
    for j in range(m):
        fila = []
        for i in range(n):
            fila.append(matriz[i][j])
        res.append(fila)
    return res


def quick_sort(lista, comparador):
    if len(lista) < 2:
        return lista
    pivot = lista[0]
    izq = []
    der = []
    for i in (lista[1:]):
        if comparador(i, pivot):
            izq.append(i)
        else:
            der.append(i)
    return quick_sort(izq, comparador) + [pivot] + quick_sort(der, comparador)


def orden(a, b):
    if (a[1] == b[1]):
        if (a[2] == b[2]):
            return a[0] < b[0]
        return a[2] > b[2]
    return a[1] > b[1]


def popularidad(publicaciones):
    publicaciones = transpuesta(publicaciones)
    publicaciones = quick_sort(publicaciones, orden)
    res = []
    for i in publicaciones:
        res.append(i[0][0])
    return res


print(popularidad([["A", "B", "C"],
                   [3, 50, 50],
                   [8, 9, 2]]))

print(popularidad([["B", "A"],
                   [100, 100],
                   [1000, 1000]]))


# Pregunta 3
def fila_nula(largo):
    return [0] * largo


def matriz_nula(filas, columnas):
    mat = []
    for _ in range(filas):
        mat.append(fila_nula(columnas))
    return mat


def identidad(n):
    mat = matriz_nula(n, n)
    for i in range(n):
        mat[i][i] = 1
    return mat


def multiplicar(matriz1, matriz2):
    filas1 = len(matriz1)
    columnas1 = len(matriz1[0])
    columnas2 = len(matriz2[0])
    resultado = matriz_nula(filas1, columnas2)
    for i in range(filas1):
        for j in range(columnas2):
            for k in range(columnas1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return resultado


def exponenciar(matriz, n):
    if n == 0:
        return identidad(len(matriz))
    mm = exponenciar(matriz, n // 2)
    res = multiplicar(mm, mm)
    if n % 2:
        return multiplicar(res, matriz)
    return res


def mif(n):
    ''' con n = 4
    [0, 1, 0,  0]   [f(n-4)]   [f(n-3)]
    [0, 0, 1,  0]   [f(n-3)]   [f(n-2)]
    [0, 0, 0,  1]   [f(n-2)]   [f(n-1)]
    [-2, 1, 0, 3] * [f(n-1)] = [f(n)  ]
    '''
    mat = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [-2, 1, 0, 3]
    ]
    casos_base = [
        [1],
        [2],
        [10],
        [15]
    ]
    return multiplicar(exponenciar(mat, n), casos_base)[0][0]


print(mif(2))
print(mif(5))


# Pregunta 4
def acumulada(matriz):
    n, m = len(matriz), len(matriz[0])
    res = matriz_nula(n + 1, m + 1)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            res[i][j] = matriz[i-1][j-1] + \
                res[i-1][j] + res[i][j-1] - res[i-1][j-1]
    return res


def range_query(matacumulada, r1, c1, r2, c2):
    return matacumulada[r2 + 1][c2 + 1] - matacumulada[r1][c2 + 1] - matacumulada[r2 + 1][c1] + matacumulada[r1][c1]


def subMatMax(matriz):
    matacumulada = acumulada(matriz)
    n, m = len(matriz), len(matriz[0])
    res = -1
    coordenada = [(-1, -1), (-1, -1)]
    for k in range(1, n):
        tamano = k - 1
        for i in range(n - tamano):
            for j in range(m - tamano):
                local = range_query(matacumulada, i, j, i + tamano, j + tamano)
                if not (local % 7) and local > res:
                    res = local
                    coordenada = [(i, j), (i + tamano, j + tamano)]
    return coordenada


print(subMatMax([[1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 11]]))


# Pregunta 5
def push(lista, e):
    return lista.append(e)


def pop(lista):
    return lista.pop(-1)


def isEmpty(lista):
    return len(lista) == 0


def es_solucion(inicio, fin):
    return inicio[0][0] == fin[0] and inicio[0][1] == fin[1]


def obtener_hijos(matriz, camino):
    n, m = len(matriz), len(matriz[0])
    hijos = []
    pos = camino[0]
    if pos[0] - 1 >= 0 and matriz[pos[0] - 1][pos[1]] == 0 and pos not in camino[1]:
        hijos.append(((pos[0] - 1, pos[1]), camino[1] + [pos]))
    if pos[0] + 1 < n and matriz[pos[0] + 1][pos[1]] == 0 and pos not in camino[1]:
        hijos.append(((pos[0] + 1, pos[1]), camino[1] + [pos]))
    if pos[1] - 1 >= 0 and matriz[pos[0]][pos[1] - 1] == 0 and pos not in camino[1]:
        hijos.append(((pos[0], pos[1] - 1), camino[1] + [pos]))
    if pos[1] + 1 < m and matriz[pos[0]][pos[1] + 1] == 0 and pos not in camino[1]:
        hijos.append(((pos[0], pos[1] + 1), camino[1] + [pos]))
    return hijos


def resolver(matriz, inicio, fin):
    pila = []
    push(pila, (inicio, []))

    while (not isEmpty(pila)):
        estado = pop(pila)
        if (es_solucion(estado, fin)):
            return True
        hijos = obtener_hijos(matriz, estado)
        for hijo in hijos:
            push(pila, hijo)

    return False


print(resolver([[0, 1, 0],
                [0, 1, 0],
                [0, 0, 0]],
               (0, 0), (0, 2)))
