def duplo(n):
    return n * 2

def general(a, b, c):
    return (-b + (b ** 2 - 4 * a * c) ** (0.5)) / (2 * a)

def precio_final(precio, iva=0.13):
    return precio * (1 + iva)

def valor_absoluto(n):
    if n < 0:
        return -n
    return n

def main():
    print(duplo(5))
    print(general(1, 5, 6))
    print(precio_final(101))
    print(valor_absoluto(-5))

if __name__ == "__main__":
    main()