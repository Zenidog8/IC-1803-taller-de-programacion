import turtle
"""
Para poder usar turtle en un script de python, es necesario tener instalado el módulo turtle.

Para instalar turtle, se puede usar el siguiente comando:
    sudo apt-get install -y python3-wxgtk4.0
    sudo apt-get install -y python3-tk

No ha sido probado en Windows Subsystem for Linux (WSL), pero debería funcionar.

Para ejecutar el script, se puede usar el siguiente comando:
    python3 turtle-tree.py
"""


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


def arbol_aux(lista, distancia):
    if lista == []:
        return

    elif lista[izq] == [] and lista[der] == []:
        turtle.circle(-20, 180)
        turtle.write(lista[valor], move=False,
                     align="center", font=("Arial", 15, "normal"))
        turtle.circle(-20, 180)
        turtle.circle(-20, 180)
        turtle.right(180)

    else:
        hijo_izquierdo = lista[1]
        hijo_derecho = lista[2]

        # Comprobar si ambos hijos existen
        if hijo_izquierdo != [] and hijo_derecho != []:
            arbol_aux([lista[0], [], []], distancia / 2)

            turtle.left(225)
            turtle.forward(distancia)
            turtle.left(135)

            arbol_aux(hijo_izquierdo, distancia / 2)

            turtle.circle(20, 180)
            turtle.right(135)
            turtle.forward(distancia)
            turtle.right(90)
            turtle.forward(distancia)
            turtle.left(45)

            arbol_aux(hijo_derecho, distancia / 2)

            turtle.circle(20, 180)
            turtle.right(45)
            turtle.forward(distancia)
            turtle.right(135)

        # En caso de que solo exista hijo izquierdo
        elif hijo_derecho == [] and hijo_izquierdo != []:
            arbol_aux([lista[0], [], []], distancia / 2)

            turtle.left(225)
            turtle.forward(distancia)
            turtle.left(135)

            arbol_aux(hijo_izquierdo, distancia / 2)

            turtle.circle(20, 180)
            turtle.right(135)
            turtle.forward(distancia)
            turtle.right(45)

        # En caso de que solo exista hijo derecho
        elif hijo_derecho != [] and hijo_izquierdo == []:
            arbol_aux([lista[0], [], []], distancia / 2)

            turtle.right(45)
            turtle.forward(distancia)
            turtle.left(45)

            arbol_aux(hijo_derecho, distancia / 2)

            turtle.circle(20, 180)
            turtle.right(45)
            turtle.forward(distancia)
            turtle.right(135)


def parbol(lista):

    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.forward(300)
    turtle.right(90)
    turtle.pendown()
    arbol_aux(lista, 250)
    turtle.done()


def main():
    arbol = []
    arbol = insertar(arbol, 5)
    arbol = insertar(arbol, 3)
    arbol = insertar(arbol, 7)
    arbol = insertar(arbol, 2)
    arbol = insertar(arbol, 4)
    # [5, [3, [2, [], []], [4, [], []]], [7, [], []]]
    #      5
    #     / \
    #    3   7
    #   / \
    #  2   4
    arbol = eliminar(arbol, 3)
    # [5, [4, [2, [], []], []], [7, [], []]]
    #      5
    #     / \
    #    4   7
    #   /
    #  2
    arbol = insertar(arbol, 6)
    arbol = insertar(arbol, 8)
    # [5, [4, [2, [], []], []], [7, [6, [], []], [8, [], []]]]
    #      5
    #     / \
    #    4   7
    #   /   / \
    #  2   6   8

    # Imprimir el árbol graficamente, >>solo una llamada por script<<
    parbol(arbol)


if __name__ == '__main__':
    main()
