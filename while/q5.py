list = []
i = 0
while i < 15:
    num = int(input("Digite um valor: "))
    list.append(num)
    i += 1
print(sum([n for n in list if n % 2 != 0]))