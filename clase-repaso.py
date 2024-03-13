import sys
sys.setrecursionlimit(100000)

'''
Ejercicio 1, ejecutar con un n pequeño
'''

def es_multiplo_de_siete(n):
    if n % 7 == 0:
        return 1
    return 0

def sigma_derecha(a, b):
    if a > b:
        return 0
    else:
        return es_multiplo_de_siete(a) + sigma_derecha(a + 1, b)
    
def pi_centro(a, b):
    if a > b:
        return 1
    else:
        return sigma_derecha(a, a * a * a) * pi_centro(a + 1, b)
    
def sigma_izquierda(a, b):
    if a > b:
        return 0
    else:
        return pi_centro(a, a * a) + sigma_izquierda(a + 1, b)
    

'''
Ejercicio 2, es tan grande que rompe la pila
'''

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def suma_derecha(a, b, c):
    if a > b:
        return 0
    else:
        return a * c + suma_derecha(a + 1, b, c)
    
def suma_izquierda(a, b):
    if a > b:
        return 0
    else:
        return a * suma_derecha(a, a * a * a * a, a)
    
def suma_i(a, b):
    if a > b:
        return 0
    else:
        return 4 * a + suma_i(a + 1, b)
    
def resolver(n):
    i = suma_i(1, n)
    return suma_izquierda(i, factorial(n * n))
