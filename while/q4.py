list = []
i = 0
limite = 200
minimo = 100
while i < 10:
    x = int(input("Digite um valor: "))
    list.append(x)
    i += 1
filtro = [n for n in list if minimo <= n <= limite]
print(filtro)