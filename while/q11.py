import numpy as np
n = int(input("Número: "))
soma = np.sum(1 / np.arange(1, n + 1))
print("Forma rapida: ", soma)

from decimal import Decimal, getcontext
#forma lenta
getcontext().prec = 50
n = int(input("Numero:"))
soma = sum(Decimal(1) / Decimal(i) for i in range(1, n + 1))
print("Forma lenta: ", soma)