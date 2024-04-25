def criba(n):
    primos = [1] * (n+1)
    p = 2
    while (p * p <= n):
        if (primos[p] == 1):
            for i in range(p * p, n+1, p):
                primos[i] = 0
        p += 1
    return primos


def imprimir_primos(tablero):
    for p in range(2, len(tablero)):
        if tablero[p]:
            print(p, end=" ")
    print()


def main():
    n = 100
    tablero = criba(n)
    imprimir_primos(tablero)


if __name__ == '__main__':
    main()
