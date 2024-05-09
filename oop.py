class Triangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


class Calculadora:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

    def area(self, figura):
        return figura.area()


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def agregar(self, valor):
        if self.siguiente is None:
            self.siguiente = Nodo(valor)
        else:
            self.siguiente.agregar(valor)


class Lista:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        if self.cabeza is None:
            self.cabeza = Nodo(valor)
        else:
            self.cabeza.agregar(valor)

    def imprimir(self):
        nodo = self.cabeza
        while nodo is not None:
            print(nodo.valor, end=" -> ")
            nodo = nodo.siguiente
        print("None")


print(Calculadora().suma(1, 2))

unTriangulo = Triangulo(3, 4)

print(unTriangulo.area())

print(Calculadora().area(unTriangulo))

unaLista = Lista()

unaLista.agregar(1)
unaLista.agregar(2)
unaLista.agregar(3)

unaLista.imprimir()


class Perro:
    # Variable compartida por todas las instancias de la clase
    especie = "Canis familiaris"

    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def __str__(self):
        return f"{self.nombre} es un {self.raza}"


mi_perro = Perro("Firulais", "Dálmata")
el_perro_de_mi_vecino = Perro("Rex", "Pastor Alemán")

print(mi_perro, "->", mi_perro.especie)
print(el_perro_de_mi_vecino, "->", el_perro_de_mi_vecino.especie)
