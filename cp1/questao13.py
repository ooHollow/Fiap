import numpy as np

def calculo(a, b, c):
    if a == 0:
        print("A não pode ser igual a 0")
        return
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Não há raizes reais.")
        return
    raizes = np.roots([a, b, c])
    print(f'as raizes da equação são {raizes}')
calculo(int(input("Defina o a: ")), int(input("Defina o b: ")), int(input("Defina o c: ")))