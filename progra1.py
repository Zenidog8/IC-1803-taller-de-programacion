def validar_faccion(numerador, denominador, repeticiones):
    numero = numerador * 100000 + denominador
    digitos = [0]*10
    while numero > 0:
        digito = numero % 10
        digitos[digito] += 1
        if digitos[digito] > repeticiones:
            return False
        numero //= 10
    return True


def encontrar_faccion(numero, repeticiones):
    soluciones = []
    for denominador in range(1000, 100000):
        numerador = numero * denominador
        if numerador > 9999 and numerador < 100000 and validar_faccion(numerador, denominador, repeticiones):
            soluciones.append(f'{numerador}/{denominador}={numero}\n')
    print(''.join(soluciones))


def main():
    casos = int(input())

    for _ in range(casos):
        numero, repeticiones = map(int, input().split())
        encontrar_faccion(numero, repeticiones)


if __name__ == '__main__':
    main()
