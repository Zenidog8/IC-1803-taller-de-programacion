print('''
Escriba la funcion sumaFactores(n) que recibe
un numero natural y retorna el total de la
suma de los factores de n.
''')
# Opcion 1


def sumaFactores1(n, divisor=1, total=0):
    if divisor > n:
        return total
    if n % divisor == 0:
        total += divisor
    return sumaFactores1(n, divisor + 1, total)


print(sumaFactores1(2))
print(sumaFactores1(10))

# Opcion 2


def sumaFactoresAux(n, divisor):
    if divisor*divisor > n:
        return 0
    if divisor*divisor == n:
        return divisor
    if n % divisor == 0:
        return divisor + (n // divisor) + sumaFactoresAux(n, divisor + 1)
    return sumaFactoresAux(n, divisor + 1)


def sumaFactores2(n):
    if n == 1:
        return n
    return n + 1 + sumaFactoresAux(n, 2)


print(sumaFactores2(2))
print(sumaFactores2(10))

print('''
Juan es un obsesionado con el numero 7 y le
encantan las sumas de potencias. Ha llamado a
los numeros que suman 7 potencias de 2 distintas
como los potentes. Escriba una funcion denominada
potentes(n) que retorne True si el numero
es una suma de 7 potencias de dos, y False si no
es el caso.
''')
# Si el numero tiene 7 bits prendidos (1) es potente


def potentes(n, potencias=0):
    if n == 0 and potencias == 7:
        return True
    elif n == 0 and potencias != 7:
        return False
    acumulado = potencias + n % 2  # n % 2 suma 1 o 0, al igual que pasando a binario
    return (potentes(n // 2, acumulado))


print(potentes(17))
print(potentes(127))
print(potentes(128))

print('''
Sin utilizar for o while, escriba una funcion
(o varias) que sean equivalentes a la expresion
indicada. (recibe como parametro el n), siendo
este natural y mayor que cero. La funcion debe
denominarse sumR(n).
''')

# Opcion 1


def fac(n):
    if (n < 2):
        return 1
    return n * fac(n - 1)


def suma_indice(n, k):
    if (n < k):
        return 1
    return (2 * k) * suma_indice(n, k + 1)


def suma_derecha(j, i):
    if (j > i):
        return 0
    return j + suma_derecha(j + 1, i)


def suma_izq(i, n):
    if (i > n):
        return 0
    return (i * suma_derecha(i, i * i)) + suma_izq(i + 1, n)


def sum_r(n):
    i = suma_indice(1, n)
    suma = suma_izq(i, fac(4 * n * n))
    return suma


print(sum_r(1))

# Opcion 2


def fact(n, res=1):
    if (n < 2):
        return res
    res *= n
    return fact(n-1, res)


def sumR(n):
    return sumAux(fact(n)*(1 << n), fact(4*n*n))


def sumAux(ini, fin):
    if (ini > fin):
        return 0
    return ini*sum2(ini, ini*ini) + sumAux(ini+1, fin)


def sum2(ini, fin):
    return (fin*(fin+1) - (ini-1)*ini)//2  # Por Gauss (suma de 1 a n) = n(n+1)/2


print(sumR(1))


print('''
Se tiene la funcion f(x) = x^5 + 3x^4 + 2x^2 +
x+9, dados dos puntos a y b, se desea encontrar
c tal que f(a) - f(c) = f(c) - f(b). Escriba la
funcion mediaF(a,b) que retorna el c con un error
maximo de 3 decimales (0.000), que cumple lo
especificado.
''')


def valor_absoluto(n):
    if n < 0:
        return -n
    return n


def fun(x):
    return ((x*x*x*x*x)+(3*x*x*x*x)+(2*x*x+x)+9)


def distancia(a, b):
    return valor_absoluto(a-b)


def mediaFAux(a, b, inf, sup):
    c = (inf + sup) / 2
    if (sup - inf < 0.0001):
        return c
    if (distancia(fun(a), fun(c)) > distancia(fun(b), fun(c))):
        return mediaFAux(a, b, inf, c)
    return mediaFAux(a, b, c, sup)


def mediaF(a, b):
    if (a > b):
        return mediaFAux(b, a, b, a)
    return mediaFAux(a, b, a, b)


print(mediaF(1, 1))
print(mediaF(1, 2))
print(mediaF(2, 1))
