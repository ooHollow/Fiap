i = 0
lista = []
soma = 0
while i < 10:
    x = int(input("Digite um numero: "))
    lista.append(x)
    i+=1
print(sum(lista)/len(lista))
for num in lista:
    if num % 2 == 0:
        soma += num
print(soma)