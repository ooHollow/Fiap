from collections import Counter
import random
def dado():
    lista = [random.randint(1, 6) for _ in range(1000000)]
    return Counter(lista)
print(dado())