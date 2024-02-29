def calcular_largo(lista):
    """Calcula el largo de una lista"""
    if lista == []:
        return 0

    return 1 + calcular_largo(lista[1:])


def calcular_suma(lista):
    """Calcula la suma de todos los números en una lista"""
    if lista == []:
        return 0

    return lista[0] + calcular_suma(lista[1:])


def buscar_elemento(lista, elemento):
    """Busca un elemento en una lista"""
    if lista == []:
        return False
    if lista[0] == elemento:
        return True

    return buscar_elemento(lista[1:], elemento)


def main():
    """Funcion principal que imprime los resultados de las funciones anteriores"""
    lista = [1, 2, 3, 4, 5]
    print(calcular_largo(lista))
    print(calcular_suma(lista))
    print(buscar_elemento(lista, 43))


# Si el archivo es ejecutado directamente, se llama a la funcion main
if __name__ == "__main__":
    main()
