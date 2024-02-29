def binario_a_decimal(binario, decimal=0, i=0):
    '''Convierte un número binario a decimal'''
    if binario == 0:
        return decimal
    
    digito = binario % 10
    decimal = decimal + digito * (2 ** i)
    binario = binario // 10
    return binario_a_decimal(binario, decimal, i + 1)


def decimal_a_binario(decimal):
    '''Convierte un número decimal a binario'''
    if decimal == 0:
        return 0

    return (decimal % 2 + 10 * decimal_a_binario(decimal // 2))


def potencia(base, exponente):
    '''Calcula la potencia de un número usando exponenciación logarítmica'''
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base

    media_potencia = potencia(base, exponente // 2)
    resultado = media_potencia * media_potencia
    if exponente % 2 == 1:
        resultado *= base
    return resultado


def main():
    '''Funcion principal que imprime los resultados de las funciones anteriores'''
    binario = 10111
    decimal = binario_a_decimal(binario)
    print("El número binario", binario, "es", decimal, "en decimal")
    decimal = 47
    binario = decimal_a_binario(decimal)
    print("El número decimal", decimal, "es", binario, "en binario")
    elevado = potencia(2, 8)
    print("2 elevado a 8 es", elevado)


# Si el archivo es ejecutado directamente, se llama a la funcion main
if __name__ == "__main__":
    main()
