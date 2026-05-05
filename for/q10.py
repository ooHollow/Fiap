a = int(input("Digite um numero: "))
n = int(input("Digite um numero: "))
for i in range(1,a+1):
    soma = 0
    lista = []
    for x in range(1,n+1):
        notas = int(input("Digite um numero: "))
        lista.append(notas)
    print(sum(lista) / len(lista))