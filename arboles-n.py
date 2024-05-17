arbol = [100, [[4, []], [8, [[5, []]]], [34, []]]]
#   100
#  / | \
# 4  8  34
#    |
#    5

'''
Recorrido por anchura de un árbol n-ario
'''


def recorrido_anchura(arbol):
    cola = [arbol]
    while cola:
        nodo = cola.pop(0)
        print(nodo[0], end=" ")
        for i in range(len(nodo[1])):
            if nodo[1][i]:
                cola.append(nodo[1][i])
    print()


print("recorrido_anchura", end=' ')  # 100 4 8 34 5
recorrido_anchura(arbol)

'''
Recorrido por profundidad de un árbol n-ario
'''


def recorrido_profundidad(arbol):
    pila = [arbol]
    while pila:
        nodo = pila.pop()
        print(nodo[0], end=" ")
        for i in range(len(nodo[1])):
            if nodo[1][i]:
                pila.append(nodo[1][i])
    print()


print("recorrido_profundidad", end=' ')  # 100 34 8 5 4
recorrido_profundidad(arbol)

'''
Contar los nodos de un arbol n-ario
'''


def contar_nodos(arbol):
    res = 1
    if arbol == []:
        return 0
    for nodo in arbol[1]:
        res += contar_nodos(nodo)
    return res


print("contar_nodos", contar_nodos(arbol))  # 5

'''
Retornar el nivel donde se encuentra un nodo n en un arbol n-ario, -1 si no existe
'''


def nivel_nodo(arbol, n):
    if arbol == []:
        return -1
    if arbol[0] == n:
        return 0
    for nodo in arbol[1]:
        nivel = nivel_nodo(nodo, n)
        if nivel != -1:
            return 1 + nivel
    return -1


print("nivel_nodo", nivel_nodo(arbol, 5))  # 2

'''
Retornar una lista con la suma de los nodos de un nivel de un arbol n-ario
'''


def altura(arbol):
    subaltura = 0
    if arbol == []:
        return 0
    for nodo in arbol[1]:
        subaltura = max(subaltura, altura(nodo))
    return 1 + subaltura


def suma_nivel_aux(arbol, nivel):
    if arbol == []:
        return 0
    if nivel == 0:
        return arbol[0]
    res = 0
    for nodo in arbol[1]:
        res += suma_nivel_aux(nodo, nivel-1)
    return res


def suma_nivel(arbol):
    niveles = altura(arbol)
    res = [0] * niveles
    for nivel in range(niveles):
        res[nivel] = suma_nivel_aux(arbol, nivel)
    return res


print("suma_nivel", suma_nivel(arbol))  # [100, 46, 5]
