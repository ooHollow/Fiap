import random
lista = []
for n in range(11):
    x = random.randint(1, 10)
    lista.append(x)
i = int(input("Insira um número (De 1 a 10): "))
print("Esse número aparece:", lista.count(i), "vezes.")
print(lista)