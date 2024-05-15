arbol = [5, [4, [2, [], []], []], [7, [6, [], []], [8, [], []]]]
#      5
#     / \
#    4   7
#   /   / \
#  2   6   8

valor = 0
izq = 1
der = 2

"""
En un arbol binario de busqueda, se desea encontrar la suma del menor y mayor valor del arbol.
"""


def encontrar_menor(arbol):
    if arbol[izq] == []:
        return arbol[valor]
    return encontrar_menor(arbol[izq])


def encontrar_mayor(arbol):
    if arbol[der] == []:
        return arbol[valor]
    return encontrar_mayor(arbol[der])


def suma_menor_mayor(arbol):
    return encontrar_menor(arbol) + encontrar_mayor(arbol)


print("suma del menor y mayor valor del arbol:", suma_menor_mayor(arbol))  # 10


"""
Retorne la altura del subarbol que tenga como raiz el valor n, si el valor no existe retorne -1.
"""


def altura(arbol):
    if arbol == []:
        return 0
    return 1 + max(altura(arbol[izq]), altura(arbol[der]))


def altura_n(arbol, n):
    if arbol == []:
        return -1
    if arbol[valor] == n:
        return altura(arbol)
    return max(altura_n(arbol[izq], n), altura_n(arbol[der], n))


print("altura del subarbol que tenga como raiz el valor 7:", altura_n(arbol, 7))  # 2
print("altura del subarbol que tenga como raiz el valor 20:",
      altura_n(arbol, 20))  # -1


"""
Invierta el arbol.
"""


def invertir_arbol(arbol):
    if arbol == []:
        return []
    return [arbol[valor], invertir_arbol(arbol[der]), invertir_arbol(arbol[izq])]


# [5, [7, [8, [], []], [6, [], []]], [4, [], [2, [], []]]]
print("Invierta el arbol:", invertir_arbol(arbol))
#      5
#     / \
#    7   4
#   / \   \
#  8   6   2


"""
Retorne la media de la suma de los valores del camino mas largo del arbol.
"""

arbol2 = [5, [4, [2, [], []], []], [7, [], []]]
#      5
#     / \
#    4   7
#   /
#  2


def camino_mas_largo(arbol):
    if arbol == []:
        return 0
    if altura(arbol[izq]) > altura(arbol[der]):
        return arbol[valor] + camino_mas_largo(arbol[izq])
    return arbol[valor] + camino_mas_largo(arbol[der])


def media_camino_mas_largo(arbol):
    return camino_mas_largo(arbol) / altura(arbol)


print("media de la suma de los valores del camino mas largo del arbol:",
      media_camino_mas_largo(arbol2))  # 3.6
