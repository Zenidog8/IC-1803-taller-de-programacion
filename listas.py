def sqrt_aux(n, inf, sup, err=0.00000000001):
    m = (inf + sup) / 2

    if sup - inf <= err or m * m == n:
        return m
    
    if m * m > n:
        return sqrt_aux(n, inf, m, err)
    else:
        return sqrt_aux(n, m, sup, err)


def sqrt(n):
    return sqrt_aux(n, 0, n)


def quick_sort(lista):
  if lista == []:
    return []
  pivot = lista[len(lista) // 2]
  centro = []
  izq = []
  der = []
  for i in range(len(lista)):
    if lista[i] < pivot:
      izq.append(lista[i])
    elif lista[i] == pivot:
      centro.append(lista[i])
    else:
      der.append(lista[i])
  return quick_sort(izq) + centro + quick_sort(der)


def media(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma / len(lista)


def mediana(lista):
    lista = quick_sort(lista)
    n = len(lista)
    if n % 2 == 0:
        return (lista[n // 2 - 1] + lista[n // 2]) / 2
    else:
        return lista[n // 2]


def norma(lista):
    suma = 0
    for elemento in lista:
        suma += (elemento * elemento)
    return sqrt(suma)


def moda(lista):
    if len(lista) == 1:
        return lista[0]
    
    lista = quick_sort(lista)
    res, actual = lista[0], lista[0]
    maximo,contador = 1, 1

    for i in range(1, len(lista)):
        if lista[i] == actual:
            contador += 1
        else:
            if contador > maximo:
                res = actual
                maximo = contador
            actual = lista[i]
            contador = 1
    return res


def main():
    lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print("Media:", media(lista))
    print("Mediana:", mediana(lista))
    print("Norma:", norma(lista))
    print("Moda:", moda(lista))


if __name__ == "__main__":
    main()