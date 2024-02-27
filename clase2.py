def duplo(n):
    '''
    Funcion que recibe un numero y devuelve el doble de ese numero
    '''
    return n * 2


def general(a, b, c):
    '''
    Funcion que recibe los coeficientes de una ecuacion cuadratica y devuelve el valor de x
    '''
    return (-b + (b ** 2 - 4 * a * c) ** (0.5)) / (2 * a)


def precio_final(precio, iva=0.13):
    '''
    Funcion que recibe el precio de un producto y devuelve el precio final con el porcentaje de IVA (13% por defecto)
    Nota: Se puede optimizar sacando el precio como factor común de la multiplicación, pero se deja asi para que sea mas claro
    '''
    return precio + (precio * iva)


def valor_absoluto(n):
    '''
    Funcion que recibe un numero y devuelve su valor absoluto
    '''
    if n < 0:
        return -n
    return n


def main():
    '''
    Funcion principal que imprime los resultados de las funciones anteriores
    '''
    print(duplo(5))
    print(general(1, 5, 6))
    print(precio_final(101))
    print(valor_absoluto(-5))


# Si el archivo es ejecutado directamente, se llama a la funcion main
if __name__ == "__main__":
    main()
