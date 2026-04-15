import random
i = 0
lista = []
while i < 20:
    x = random.randint(1, 50)
    lista.append(x)
    i+=1
print(max(lista), min(lista))