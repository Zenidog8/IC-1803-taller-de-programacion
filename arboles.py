valor = 0
izq = 1
der = 2


def crear_nodo(dato):
    return [dato, [], []]


def insertar(arbol, dato):
    if arbol == []:
        return crear_nodo(dato)
    if dato < arbol[valor]:
        arbol[izq] = insertar(arbol[izq], dato)
    else:
        arbol[der] = insertar(arbol[der], dato)
    return arbol


def buscar(arbol, dato):
    if arbol == []:
        return False
    if arbol[valor] == dato:
        return True
    if dato < arbol[valor]:
        return buscar(arbol[izq], dato)
    return buscar(arbol[der], dato)


def eliminar(arbol, dato):
    if arbol == []:
        return []
    if arbol[valor] == dato:
        if arbol[izq] == [] and arbol[der] == []:
            return []
        if arbol[izq] == []:
            return arbol[der]
        if arbol[der] == []:
            return arbol[izq]
        arbol[valor] = encontrar_menor(arbol[der])
        arbol[der] = eliminar(arbol[der], arbol[valor])
        return arbol
    if dato < arbol[valor]:
        arbol[izq] = eliminar(arbol[izq], dato)
    else:
        arbol[der] = eliminar(arbol[der], dato)
    return arbol


def encontrar_menor(arbol):
    if arbol[izq] == []:
        return arbol[valor]
    return encontrar_menor(arbol[izq])


arbol = []
arbol = insertar(arbol, 5)
arbol = insertar(arbol, 3)
arbol = insertar(arbol, 7)
arbol = insertar(arbol, 2)
arbol = insertar(arbol, 4)

print(arbol)
# [5, [3, [2, [], []], [4, [], []]], [7, [], []]]
#      5
#     / \
#    3   7
#   / \
#  2   4

arbol = eliminar(arbol, 3)
print(arbol)
# [5, [4, [2, [], []], []], [7, [], []]]
#      5
#     / \
#    4   7
#   /
#  2

arbol = insertar(arbol, 6)
arbol = insertar(arbol, 8)

print(arbol)
# [5, [4, [2, [], []], []], [7, [6, [], []], [8, [], []]]]
#      5
#     / \
#    4   7
#   /   / \
#  2   6   8

arbol = eliminar(arbol, 5)
print(arbol)
# [6, [4, [2, [], []], []], [7, [], [8, [], []]]]
#      6
#     / \
#    4   7
#   /     \
#  2       8


def altura(arbol):
    if arbol == []:
        return 0
    return 1 + max(altura(arbol[izq]), altura(arbol[der]))


print("altura:", altura(arbol))


def inorden(arbol):
    if arbol == []:
        return []
    return inorden(arbol[izq]) + [arbol[valor]] + inorden(arbol[der])


print("inorden:", inorden(arbol))


def preorden(arbol):
    if arbol == []:
        return []
    return [arbol[valor]] + preorden(arbol[izq]) + preorden(arbol[der])


print("preorden:", preorden(arbol))


def postorden(arbol):
    if arbol == []:
        return []
    return postorden(arbol[izq]) + postorden(arbol[der]) + [arbol[valor]]


print("postorden:", postorden(arbol))


def es_arbol_binario_busqueda(arbol):
    if arbol == []:
        return True
    if arbol[izq] != [] and arbol[izq][valor] > arbol[valor]:
        return False
    if arbol[der] != [] and arbol[der][valor] < arbol[valor]:
        return False
    return es_arbol_binario_busqueda(arbol[izq]) and es_arbol_binario_busqueda(arbol[der])


print("es_arbol_binario_busqueda:", es_arbol_binario_busqueda(arbol))


def es_arbol_lleno(arbol):
    if arbol == []:
        return True
    if arbol[izq] == [] and arbol[der] != []:
        return False
    if arbol[izq] != [] and arbol[der] == []:
        return False
    return es_arbol_lleno(arbol[izq]) and es_arbol_lleno(arbol[der])


print("es_arbol_lleno:", es_arbol_lleno(arbol))


def es_arbol_balanceado(arbol):
    if arbol == []:
        return True
    return abs(altura(arbol[izq]) - altura(arbol[der])) < 2 and es_arbol_balanceado(arbol[izq]) and es_arbol_balanceado(arbol[der])


print("es_arbol_balanceado:", es_arbol_balanceado(arbol))
